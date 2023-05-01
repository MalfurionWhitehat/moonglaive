#!/usr/bin/env python3

import argparse
from tabulate import tabulate

from moonglaive.platforms.code4rena import Code4rena
from moonglaive.platforms.sherlock import Sherlock

parser = argparse.ArgumentParser(
    description='Three-bladed weapon of the night elf Sentinels.')
parser.add_argument('--active', help='Active audit contests',
                    action=argparse.BooleanOptionalAction)
parser.add_argument('--upcoming', help='Upcoming audit contests',
                    action=argparse.BooleanOptionalAction)
parser.add_argument('--discord-authorization',
                    help='Discord authorization key, used to fetch server activity')
args = parser.parse_args()

filters = []
if (args.active):
    filters.append('active')
if (args.upcoming):
    filters.append('upcoming')

code4rena = Code4rena(args.discord_authorization)
sherlock = Sherlock(args.discord_authorization)
contests = code4rena.get_contests(filters) + sherlock.get_contests(filters)


header = ['platform', 'title', 'eta', 'reward']
colalign = ['left', 'left', 'right', 'right']
if args.discord_authorization is not None:
    header += ['channel.name', 'channel.users', 'channel.messages']
    colalign += ['right', 'right', 'right']

rows = []
for contest in contests:
    row = []
    for col in header:
        if '.' in col:
            [first, second] = col.split('.')
            row.append(contest[first][second])
        else:
            row.append(contest[col])
    rows.append(row)


print(tabulate(rows,
               header,
               tablefmt='grid',
               colalign=colalign))
