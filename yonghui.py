import json
import urllib
from urllib import request

from xlutils.copy import copy as xl_copy

import requests
import xlrd
from lxml import etree

url = 'http://www.yonghui.com.cn/2008_store.asp'
page = urllib.request.urlopen(url)
# page_info = page.read()
page_info = page.read().decode('GBK')
html = etree.HTML(page_info)
# print(page)
prvitems = html.xpath('//table/tr[2]/td[1]/table/tr/td/a/span/strong/span/text()')

print(prvitems)

# print(page)
