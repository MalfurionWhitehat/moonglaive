from dateutil import parser as date
from datetime import datetime


class Base():
    def __init__(self):
        pass

    def transform(self, contests):
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
                        if contest['upcoming'] else ''
                        }),
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
                            'reward': "${:,.0f}".format(contest['reward'])
                            }),
                    contests
                    )
                )
        )
        return contests
