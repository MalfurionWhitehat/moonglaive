import argparse
from tabulate import tabulate

from platforms.code4rena import Code4rena
from platforms.sherlock import Sherlock

parser = argparse.ArgumentParser(
    description='Three-bladed weapon of the night elf Sentinels.')
parser.add_argument('--active', help='Active audit contests',
                    action=argparse.BooleanOptionalAction)
parser.add_argument('--upcoming', help='Upcoming audit contests',
                    action=argparse.BooleanOptionalAction)
args = parser.parse_args()

filters = []
if (args.active):
    filters.append('active')
if (args.upcoming):
    filters.append('upcoming')

contests = Code4rena().get_contests(filters) + Sherlock().get_contests(filters)


header = ['platform', 'title', 'eta', 'reward', 'channel', 'users']
rows = [
    [contest['platform'],
     contest['title'],
     contest['eta'],
     contest['reward'],
     contest['channel']['name'],
     contest['channel']['users']]
    for contest in contests]

print(tabulate(rows,
               header,
               tablefmt='grid',
               colalign=['left', 'left', 'right', 'right', 'right', 'right']))
