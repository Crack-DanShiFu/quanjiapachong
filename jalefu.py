import json
from xlutils.copy import copy as xl_copy

import requests
import xlrd
from lxml import etree

# headers1 = {
#     'Cookie': 'ASP.NET_SessionId=jhnvjpu5sr25g0zmlmuajhxm; Hm_lvt_ad969e28d61c1bff627763d1cccefe7b=1553850138,1553852124; __utma=95004995.1479940535.1553853139.1553853139.1553853139.1; __utmc=95004995; __utmz=95004995.1553853139.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); Hm_lpvt_ad969e28d61c1bff627763d1cccefe7b=1553853147; _C4CookieKeyCity=%e5%8c%97%e4%ba%ac; _C4CookieKeyCityNum=2; __utmt=1; __utmb=95004995.3.10.1553853139',
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
# }
# params = [
#     {'CityName_CN': '中山'}
# ]
# page = requests.post(url2, headers=headers1, data=json.dumps(params))

# def sss(id):
#     url = 'http://www.carrefour.com.cn/Store/Store.aspx'
#     headers = {
#         'Cookie': 'ASP.NET_SessionId=jhnvjpu5sr25g'
#                   '0zmlmuajhxm; Hm_lvt_ad969e28d61c1bff627763d1c'
#                   'ccefe7b=1553850138,1553852124; __utmt=1; __utm'
#                   'a=148273317.1197965028.1553852256.1553852256.1553'
#                   '852256.1; __utmc=148273317; __utmz=148273317.1553'
#                   '852256.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd='
#                   '(none); __utmb=148273317.2.10.1553852256; Hm_lpv'
#                   't_ad969e28d61c1bff627763d1cccefe7b=1553852294; _'
#                   'C4CookieKeyCity=%e6%b7%b1%e5%9c%b3; _C4'
#                   'CookieKeyCityNum='+str(id),
#         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
#     }
#     page = requests.get(url, headers=headers).text
#     # page_info = page.read().decode('utf8')
#     html = etree.HTML(page)
#     print(page)
#     prvitems = html.xpath('//tbody/tr/td[1]/a/text()')
#     print(prvitems)
#
# sss(1)

url = 'http://www.carrefour.com.cn/Store/Store.aspx'
page = requests.get(url).text
# page_info = page.read().decode('utf8')
html = etree.HTML(page)
# print(page)
prvitems = html.xpath('//dd/a/text()')[0:-4]
rb = xlrd.open_workbook('all.xls', formatting_info=True)
# make a copy of it
wb = xl_copy(rb)
sheet = wb.add_sheet('家乐福')  # 在打开的excel中添加一个sheet
n = 0
for i in prvitems:
    sheet.write(n, 0, i)
    n += 1
    print(i)
wb.save('all.xls')
