import gzip
import urllib
from io import BytesIO
from urllib import request
from xlutils.copy import copy as xl_copy

import xlrd
from lxml import etree

import requests
import json

url = 'http://www.wandaplaza.cn/'
page = urllib.request.urlopen(url)
page_info = page.read()
buff = BytesIO(page_info)
f = gzip.GzipFile(fileobj=buff)
res = f.read().decode('utf-8')
# print(res)
html = etree.HTML(res)
prvitems = html.xpath('//div[@class="city ohz"]/div[@class="col"]/div/div[@class="cityBox"]/h3/text()')
cityitemsul = html.xpath('//div[@class="city ohz"]/div[@class="col"]/div/div[@class="cityBox"]/ul')
presult = {}
for u in range(len(cityitemsul)):
    presult[prvitems[u]] = len(cityitemsul[u].xpath("li/a/text()") + cityitemsul[u].xpath("li/span/text()"))

rb = xlrd.open_workbook('all.xls', formatting_info=True)
# make a copy of it
wb = xl_copy(rb)
sheet = wb.add_sheet('万达广场')  # 在打开的excel中添加一个sheet
n = 0
for r in presult:
    sheet.write(n, 0, r)
    sheet.write(n, 1, presult[r])
    n += 1
#
#
all = {}
for u in range(len(cityitemsul)):
    all[prvitems[u]] = {}
    a = cityitemsul[u].xpath("li/a/text()") + cityitemsul[u].xpath("li/span/text()")
    for i in a:
        if all[prvitems[u]].get(i[0:2]) is None:
            all[prvitems[u]][i[0:2]] = 0
        all[prvitems[u]][i[0:2]] += 1
# print(all)
n += 1
for i in range(4, len(all)):
    sheet.write(n, 0, prvitems[i])
    sheet.write(n, 1, presult[prvitems[i]])
    n += 1
    for j in all[prvitems[i]]:
        sheet.write(n, 0, j)
        sheet.write(n, 1, all[prvitems[i]][j])
        n += 1
    n += 1
    # print(all[prvitems[i]])

wb.save('all.xls')
