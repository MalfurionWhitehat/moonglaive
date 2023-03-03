import argparse
import os
from tabulate import tabulate

from platforms.code4rena import Code4rena
from platforms.sherlock import Sherlock
from services.discord import Discord

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


# print(Discord(os.environ['AUTHORIZATION']).get_users_count_from_messages(
#     'XX'))


header = ['platform', 'title', 'eta', 'reward']
rows = [
    [contest['platform'],
     contest['title'],
     contest['eta'],
     contest['reward']]
    for contest in contests]

print(tabulate(rows,
               header,
               tablefmt='grid',
               colalign=['left', 'left', 'right', 'right']))
