from typing import Dict, List
import requests

from moonglaive.platforms.base import Base


class Sherlock(Base):
    discord_guild_id = '812037309376495636'

    def __init__(self, discord_authorization: str):
        super().__init__(discord_authorization)

    def get_contests(self, filters: List[str]) -> List[Dict]:
        response = requests.get(
            url="https://mainnet-contest.sherlock.xyz/contests")
        body = response.json()
        contests = list(
            map(lambda contest:
                dict(contest,
                     **{
                         'start_timestamp': contest['starts_at'],
                         'end_timestamp': contest['ends_at'],
                         'reward': contest['prize_pool'],
                         'platform': 'Sherlock'
                     }),
                body
                )
        )
        return self.transform(contests, filters)
