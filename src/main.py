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

contests = filter(
    lambda contest: contest['active'] or contest['upcoming'] if
    args.active or args.upcoming else True,
    Code4rena().get() + Sherlock().get()
)


header = ['title', 'start_time', 'end_time', 'eta']
rows = [[contest['title'], contest['start_time'],
         contest['end_time'], contest['eta']] for contest in contests]

print(tabulate(rows, header, tablefmt='grid'))
