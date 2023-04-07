import re
from typing import Dict
from datetime import datetime
from fuzzywuzzy import fuzz

from services.discord import Channel, Discord


class Base():
    discord_guild_id = None
    discord = None
    channels = []

    def __init__(self, discord_authorization: str):
        if discord_authorization:
            self.discord = Discord(discord_authorization)
            self.channels = self.discord.get_channels(self.discord_guild_id)

    def transform(self, contests, filters):
        contests = list(
            map(lambda contest:
                dict(contest,
                     **{'eta':
                        "{:.0f}".format((contest['end_timestamp']
                                         -
                                         datetime.now()
                                         .timestamp())/60/60//24) + '-'
                        if contest['active'] else
                        "{:.0f}".format((contest['start_timestamp']
                                         -
                                         datetime.now()
                                         .timestamp())/60/60//24) + '+'
                        if contest['upcoming'] else '',
                        'channel': self.get_discord_channel(contest)
                        }),
                filter(
                    lambda contest: (contest['active'] and 'active'
                                     in filters or
                                     contest['upcoming'] and 'upcoming'
                                     in filters) if
                    (contest['active'] or contest['upcoming']) else False,
                    map(lambda contest:
                        dict(contest,
                             **{'active': contest['end_timestamp'] >
                                datetime.now().timestamp() and
                                contest['start_timestamp'] <
                                datetime.now().timestamp(),
                                'upcoming': contest['end_timestamp'] >
                                datetime.now().timestamp() and
                                contest['start_timestamp'] >
                                datetime.now().timestamp(),
                                'start_time': datetime.
                                fromtimestamp(contest['start_timestamp']),
                                'end_time': datetime.
                                fromtimestamp(contest['end_timestamp']),
                                'reward': "${:,.0f}".format(contest['reward']),
                                }),
                        contests
                        )
                )
                )
        )
        return contests

    def get_discord_channel(self, contest: Dict) -> Channel:
        channels_with_specific_date = list(
            filter(lambda channel:
                   contest['start_time'].strftime('%b-%-d').lower() in channel['name'] or
                   contest['start_time'].strftime('%b%d').lower() in channel['name'], self.channels)
        )

        contest_approx_channel_name = re.sub(
            ' +', '-',
            (re.sub(
                'contest',
                '',
                contest['title'],
                flags=re.IGNORECASE) + '-' + contest['start_time'].strftime('%b-%d')
             ).lower()
        )

        fuzz_ratio_list = list(map(lambda channel: fuzz.ratio(
            contest_approx_channel_name, channel['name']),
            channels_with_specific_date))

        if fuzz_ratio_list:
            max_value = max(fuzz_ratio_list)
            index = fuzz_ratio_list.index(max_value)
            channel = channels_with_specific_date[index]
            return dict(channel,
                        **{
                            'users': self.discord.
                            get_users_count_from_messages(channel['id'])
                        })
        else:
            return {
                'id': '',
                'name': '',
                'users': ''
            }
