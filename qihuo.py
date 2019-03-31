import urllib
from urllib import request

url = 'http://www.cfachina.org/ggxw/xhdt/index.html'
from lxml import etree

page = urllib.request.urlopen(url)
page_info = page.read().decode('utf8')
html = etree.HTML(page_info)
# print(page)
prvitems = html.xpath('//ul[@class="nr_neirong"]/li/span/a/text()')
print(prvitems)
