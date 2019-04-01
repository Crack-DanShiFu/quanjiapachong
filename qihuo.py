import urllib
from urllib import request
import re
from lxml import etree

url = 'http://www.cfachina.org/ggxw/xhdt/index.html'
page_info = urllib.request.urlopen(url).read().decode('utf8')
html = etree.HTML(page_info)
items = html.xpath('//ul[@class="nr_neirong"]/li/span/a/text()')
itemsurl = html.xpath('//ul[@class="nr_neirong"]/li/span/a/@href')
for i, val in enumerate(itemsurl):
    if re.match(r'http:', val) is None:
        itemsurl[i] = 'http://www.cfachina.org/ggxw/xhdt/' + val[2:]
print(items)
print(itemsurl)
