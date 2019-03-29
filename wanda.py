import gzip
import urllib
from io import BytesIO
from urllib import request
from lxml import etree

import requests
import json

url = 'http://www.wandaplaza.cn/'
page = urllib.request.urlopen(url)
page_info = page.read()
buff = BytesIO(page_info)
f = gzip.GzipFile(fileobj=buff)
res = f.read().decode('utf-8')
print(res)
html = etree.HTML(res)
items = html.xpath('//div[@class="city ohz"]/div[@class="col"]/div/div[@class="cityBox"]')
for i in items:
    print(i.xpath('//h3/text()'))
