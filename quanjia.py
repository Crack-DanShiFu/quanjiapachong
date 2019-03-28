import json

import xlrd
import xlwt
from xlutils.copy import copy as xl_copy
import requests

url = 'http://www.familymart.com.cn/store/Search'

result = [1, 2, 3, 4, 5, 6, 10, 11, 12, 13]

result2 = {
    '上海',
    '苏州',
    '深圳',
    '广州',
    '杭州',
    '成都',
    '无锡',
    '北京',
    '东莞',
    '嘉兴'
}


def sss(result):
    wbk = xlwt.Workbook()
    sheet = wbk.add_sheet('全家便利店')
    n = 0
    for i in result2:
        sheet.write(n, 1, i)
        n += 1
    n = 0
    for i in result:
        parms = {
            'cid': i
        }
        html = requests.post(url, parms)
        info = json.loads(html.text)
        print(len(info['mapmsg']))
        sheet.write(n, 0, i)
        n += 1

    wbk.save('all.xls')

sss(result)

# print(info['mapmsg'])
# for i in info['mapmsg']:
#     result[i['cid']] += 1
#
# n = 1
# for i in result2:
#     result2[i] = result[str(n)]
#     n += 1
#     if n == 7:
#         n += 3
# print(result2)


# n = 0
# for i in result2:

#     n += 1
