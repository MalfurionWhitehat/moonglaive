import argparse
import requests
from dateutil import parser as date
from datetime import datetime
from tabulate import tabulate

parser = argparse.ArgumentParser(
    description='Three-bladed weapon of the night elf Sentinels.')
parser.add_argument('--active', help='Active audit contests',
                    action=argparse.BooleanOptionalAction)
parser.add_argument('--upcoming', help='Upcoming audit contests',
                    action=argparse.BooleanOptionalAction)
args = parser.parse_args()

response = requests.get(
    url="https://code4rena.com/page-data/index/page-data.json")
body = response.json()
contests = filter(
    lambda contest: contest['active'] or contest['upcoming'] if
    args.active or args.upcoming else True,
    list(
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
)

header = ['title', 'start_time', 'end_time', 'eta']
rows = [[contest['title'], contest['start_time'],
         contest['end_time'], contest['eta']] for contest in contests]

print(tabulate(rows, header, tablefmt='grid'))
