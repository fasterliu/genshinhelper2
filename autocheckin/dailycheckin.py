import sys
import genshinhelper as gh
from genshinhelper.utils import log

if len(sys.argv) <= 1:
    log.info('Please give a cookie file.')
    sys.exit()

cmdParam = sys.argv[1]
if cmdParam.find("ltoken") < 0 or cmdParam.find("ltuid") < 0:
    fp = open(sys.argv[1], 'r')
    lines = fp.readlines()
    cookie = lines[0].strip()
    fp.close()
    bWriteFileResult = True
else:
    cookie = cmdParam
    bWriteFileResult = False

g = gh.Genshin(cookie)
log.info('𒆙  Genshin Check-In Helper, v{}'.format(gh.__version__))

res = g.sign()

for i in range(len(res)):
    log.info('Check-in result for role: {}'.format(i))
    log.info('  >> Region Name : {}'.format(res[i]['region_name']))
    log.info('  >> Game UID    : {}'.format(res[i]['game_uid']))
    log.info('  >> Role Name   : {}'.format(res[i]['nickname']))
    log.info('  >> Role Level  : {}'.format(res[i]['level']))
    log.info('  >> Last Sign   : {}'.format(res[i]['today']))
    log.info('  >> Total Sign  : {}'.format(res[i]['total_sign_day']))
    log.info('  >> Reward      : {} (x{})'.format(res[i]['reward_name'], res[i]['reward_cnt']))
    log.info('  >> Reward Icon : {}'.format(res[i]['reward_icon']))
    log.info('  >> Message     : {}'.format(res[i]['status']))

    if bWriteFileResult:
        fp = open("genshin.txt", "a")
        fp.write("<pre>\n")
        fp.write('Region Name : {}\n'.format(res[i]['region_name']))
        fp.write('Game UID    : {}\n'.format(res[i]['game_uid']))
        fp.write('Role Name   : {}\n'.format(res[i]['nickname']))
        fp.write('Role Level  : {}\n'.format(res[i]['level']))
        fp.write('Last Sign   : {}\n'.format(res[i]['today']))
        fp.write('Total Sign  : {}\n'.format(res[i]['total_sign_day']))
        fp.write('Reward      : {} (x{})\n'.format(res[i]['reward_name'], res[i]['reward_cnt']))
        fp.write('Message     : {}\n'.format(res[i]['status']))
        fp.write("</pre>\n")
        fp.close()

log.info('Done.')