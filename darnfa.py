import json

import requests
import xlrd
from xlutils.copy import copy as xl_copy

all = {}


def sss(id):
    url = 'http://www.rt-mart.com.cn/ajax/getcitys'
    parm = {
        'province_no': id
    }
    html = requests.post(url, parm)
    # info = json.loads(eval("u" + "\'" + html.text + "\'"))
    info = json.loads(html.text)
    all[id] = {}
    print(id)
    for inf in info['data']:
        all[id][inf['city_no']] = inf['name']
        print('    ', all[id])


for i in range(1, 27):
    sss(i)

for i in range(35, 40, 2):
    sss(i)

prsum = {}


# print(all)
def ss(pid, cid):
    url = 'http://www.rt-mart.com.cn/ajax/getstores'
    parm = {
        'province_no': pid,
        'city_no': cid
    }
    html = requests.post(url, parm)
    # info = json.loads(eval("u" + "\'" + html.text + "\'"))
    info = json.loads(html.text)
    all[pid][cid] += ('|' + str(len(info['data'])))
    if prsum.get(pid) is None:
        prsum[pid] = 0
    prsum[pid] += len(info['data'])
    print(len(info['data']))


# print(all)
for i in all:
    # print(all[i])
    for j in all[i]:
        # print(j)
        ss(i, j)

pr = {
    1: '上海市',
    2: '江苏省',
    3: '浙江省',
    4: '安徽省',
    5: '山东省',
    6: '河北省',
    7: '天津市',
    8: '北京市',
    9: '河南省',
    10: '吉林省',
    11: '黑龙江省',
    12: '辽宁省',
    13: '内蒙古自治区',
    14: '湖北省',
    15: '湖南省',
    16: '江西省',
    17: '甘肃省',
    18: '陕西省',
    19: '四川省',
    20: '重庆市',
    21: '广东省',
    22: '海南省',
    23: '广西壮族自治区',
    24: '福建省',
    25: '云南省',
    26: '贵州省',
    35: '山西省',
    37: '青海省',
    39: '宁夏回族自治区',

}

result = {}
for p in pr:
    # print(all[p])
    result[pr[p] + '|' + str(prsum[p])] = all[p]

print(result)
# print(prsum)

rb = xlrd.open_workbook('all.xls', formatting_info=True)
# make a copy of it
wb = xl_copy(rb)
sheet = wb.add_sheet('大润发')  # 在打开的excel中添加一个sheet
n = 0
for r in result:
    sheet.write(n, 0, str(r).split('|')[0])
    sheet.write(n, 1, int(str(r).split('|')[1]))
    n += 1

n += 1
for r in result:
    sheet.write(n, 0, str(r).split('|')[0])
    sheet.write(n, 1, int(str(r).split('|')[1]))
    n += 1
    for s in result[r]:
        sheet.write(n, 0, str(result[r][s]).split('|')[0])
        sheet.write(n, 1, int(str(result[r][s]).split('|')[1]))
        n += 1
    n += 1

wb.save('all.xls')
