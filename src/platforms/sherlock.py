import requests
from datetime import datetime

from platforms.base import Base


class Sherlock(Base):
    def __init__(self):
        super().__init__()

    def get(self):
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
        return self.transform(contests)
