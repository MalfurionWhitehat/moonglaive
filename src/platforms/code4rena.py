from typing import Dict, List
import requests
from dateutil import parser as date
from re import sub
from decimal import Decimal


from platforms.base import Base


class Code4rena(Base):
    discord_guild_id = '810916927919620096'

    def __init__(self):
        super().__init__()

    def get_contests(self, filters: List[str]) -> List[Dict]:
        response = requests.get(
            url="https://code4rena.com/page-data/index/page-data.json")
        body = response.json()
        contests = list(
            map(lambda contest:
                dict(contest,
                     **{
                         'start_timestamp':  date.parse(contest['start_time']).
                         timestamp(),
                         'end_timestamp':  date.parse(contest['end_time']).
                         timestamp(),
                         'reward':  Decimal(sub(r'[^\d.]', '', contest['amount'])),
                         'platform': 'Code4rena'
                     }),
                map(lambda edge: edge['node'], body['result']
                    ['data']['contests']['edges'])
                )
        )
        return self.transform(contests, filters)
