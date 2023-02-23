import requests
from dateutil import parser as date
from datetime import datetime


class Code4rena():
    def __init__(self):
        pass

    def get(self):
        response = requests.get(
            url="https://code4rena.com/page-data/index/page-data.json")
        body = response.json()
        contests = list(
            map(lambda contest:
                dict(contest,
                     **{'eta': "{:.0f}".format((date.parse(contest['end_time'])
                                                    .timestamp() -
                                                datetime.now()
                                                    .timestamp())/60/60//24) + '-'
                        if contest['active'] else
                        "{:.0f}".format((date.parse(contest['start_time'])
                                             .timestamp() -
                                         datetime.now()
                                             .timestamp())/60/60//24) + '+'
                        if contest['upcoming'] else ''
                        }),
                map(lambda contest:
                    dict(contest,
                         **{'active': date.parse(contest['end_time']).timestamp() >
                            datetime.now().timestamp() and
                            date.parse(contest['start_time']).timestamp() <
                            datetime.now().timestamp(),
                            'upcoming': date.parse(contest['end_time']).timestamp() >
                            datetime.now().timestamp() and
                            date.parse(contest['start_time']).timestamp() >
                            datetime.now().timestamp(),
                            }),
                    map(lambda edge: edge['node'], body['result']
                        ['data']['contests']['edges'])
                    )
                )
        )
        return contests
