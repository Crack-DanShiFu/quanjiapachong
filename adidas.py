from urllib import request
from lxml import etree

import requests
import json


def get_all_citys():
    url = 'https://www.adidas.com.cn/location/storefinder'
    page = request.Request(url)
    page_info = request.urlopen(page)
    html = etree.HTML(page_info)
    items = html.xpath('//div[@class="province-event"]')
    print(items)


get_all_citys()
