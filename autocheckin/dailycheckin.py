import sys
import genshinhelper as gh
from genshinhelper.utils import log

if __name__ == "__main__":
    if len(sys.argv) < 2:
        exit(1)
    cookie = sys.argv[1]

    log.disable(log.DEBUG)
    log.disable(log.INFO)

    g = gh.Genshin(cookie)
    sign = g.sign()

    for i in range(len(sign)):
        print('Region Name : ' + str(sign[i]['region_name']))
        print('Game UID    : ' + str(sign[i]['game_uid']))
        print('Role Name   : ' + str(sign[i]['nickname']))
        print('Role Level  : ' + str(sign[i]['level']))
        print('Last Sign   : ' + str(sign[i]['today']))
        print('Total Sign  : ' + str(sign[i]['total_sign_day']))
        print('Reward      : ' + str(sign[i]['reward_name']))
        print('Message     : ' + str(sign[i]['status']))
