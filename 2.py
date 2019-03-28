import json

import xlrd
import xlwt
from xlutils.copy import copy as xl_copy
import requests

urls = {
    # '全家便利店': 'https://map.baidu.com/?newmap=1&reqflag=pcmap&biz=1&from=webmap&da_par=direct&pcevaname=pc4.1&qt=s&da_src=searchBox.button&wd=%E5%85%A8%E5%AE%B6%E4%BE%BF%E5%88%A9%E5%BA%97&c=1&src=0&wd2=&pn=0&sug=0&l=5&b=(6347177.959998436,2069076.7500023227;16832937.959998436,6910548.750002323)&from=webmap&biz_forward={%22scaler%22:1,%22styles%22:%22pl%22}&sug_forward=&auth=xG49aFzQfWWPRGDeYBSL91PwWBvGNMKQuxHHBNREBLHtfy9GUIsxAwwi04vy77u1GgvPUDZYOYIZuVt1cv3uVtGccZcuVtPWv3Guzt7xjhN%40ThwzBDGJ4P6VWvcEWe1GD8zv7u%40ZPuVteuVtegvcguxHHBNREBHLttx77IKHs99Xvy&device_ratio=1&tn=B_NORMAL_MAP&nn=0&u_loc=12535262,3089832&ie=utf-8&t=1553784367611',
    # '阿迪达斯':'https://map.baidu.com/?newmap=1&reqflag=pcmap&biz=1&from=webmap&da_par=direct&pcevaname=pc4.1&qt=s&da_src=searchBox.button&wd=%E9%98%BF%E8%BF%AA%E8%BE%BE%E6%96%AF&c=1&src=0&wd2=&pn=0&sug=0&l=5&b=(6363475.220000001,2248539.88;16849235.22,7090011.88)&from=webmap&biz_forward={%22scaler%22:1,%22styles%22:%22pl%22}&sug_forward=&auth=xG49aFzQfWWPRGDeYBSL91PwWBvGNMKQuxHHBNREBLRtBnlQADZZz1GgvPUDZYOYIZuVt1cv3uVtGccZcuVtPWv3Guzt7xjhN%40ThwzBDGJ4P6VWvcEWe1GDdw8E62qvSucFC%40B%40ZPuVteuxtf0wd0vyIICOSFCIMutx77IKHs99XvA&device_ratio=1&tn=B_NORMAL_MAP&nn=0&u_loc=12535262,3089832&ie=utf-8&t=1553784448867',
    # '大润发':'https://map.baidu.com/?newmap=1&reqflag=pcmap&biz=1&from=webmap&da_par=direct&pcevaname=pc4.1&qt=s&da_src=searchBox.button&wd=%E5%A4%A7%E6%B6%A6%E5%8F%91&c=1&src=0&wd2=&pn=0&sug=0&l=5&b=(6363475.220000001,2248539.88;16849235.22,7090011.88)&from=webmap&biz_forward={%22scaler%22:1,%22styles%22:%22pl%22}&sug_forward=&auth=xG49aFzQfWWPRGDeYBSL91PwWBvGNMKQuxHHBNRELHNtComRB199Ay1uVt1GgvPUDZYOYIZuVt1cv3uVtGccZcuVtPWv3GuBtWykiO%3DUixAC123N5T7XwcEWe1GD8zv7u%40ZPuVteuxztprGnrFHQQKW9NKQUErJj5cSEIKNHquTTGIFs99XvA&device_ratio=1&tn=B_NORMAL_MAP&nn=0&u_loc=12535262,3089832&ie=utf-8&t=1553784877577',
    # '希尔顿酒店': 'https://map.baidu.com/?newmap=1&reqflag=pcmap&biz=1&from=webmap&da_par=direct&pcevaname=pc4.1&qt=s&da_src=searchBox.button&wd=%E5%B8%8C%E5%B0%94%E9%A1%BF%E9%85%92%E5%BA%97&c=1&src=0&wd2=&pn=0&sug=0&l=5&b=(6363475.220000001,2248539.88;16849235.22,7090011.88)&from=webmap&biz_forward={%22scaler%22:1,%22styles%22:%22pl%22}&sug_forward=&auth=xG49aFzQfWWPRGDeYBSL91PwWBvGNMKQuxHHBNRETBTtwi04vy77uy1uVt1GgvPUDZYOYIZuVtcvY1SGpuEt2gz4yYxGccZcuVtPWv3GuBtWykiO%3DUixAC123N5T7XwcEWe1GD8zv7u%40ZPuVteuzztghxehwzJJDP6GDJ4vtx77IMHt%40%40YwB&device_ratio=1&tn=B_NORMAL_MAP&nn=0&u_loc=12535262,3089832&ie=utf-8&t=1553784942593',
    # '洲际酒店':'https://map.baidu.com/?newmap=1&reqflag=pcmap&biz=1&from=webmap&da_par=direct&pcevaname=pc4.1&qt=s&da_src=searchBox.button&wd=%E6%B4%B2%E9%99%85%E9%85%92%E5%BA%97&c=1&src=0&wd2=&pn=0&sug=0&l=5&b=(6363475.220000001,2248539.88;16849235.22,7090011.88)&from=webmap&biz_forward={%22scaler%22:1,%22styles%22:%22pl%22}&sug_forward=&auth=xG49aFzQfWWPRGDeYBSL91PwWBvGNMKQuxHHBNRHzTxtxjhNwzWWvy1uVt1GgvPUDZYOYIZuVt1cv3uVtGccZcuVtPWv3GuHtYAmk5b7kzC1FILPRVX8ycEWe1GD8zv7u%40ZPuVteuBLttvJrvIKTTNZbQNTXHtx77INHfy9GUIsxA2wEjjg2K&device_ratio=1&tn=B_NORMAL_MAP&nn=0&u_loc=12535262,3089832&ie=utf-8&t=1553785291752',
    # '万豪酒店':'https://map.baidu.com/?newmap=1&reqflag=pcmap&biz=1&from=webmap&da_par=direct&pcevaname=pc4.1&qt=s&da_src=searchBox.button&wd=%E4%B8%87%E8%B1%AA%E9%85%92%E5%BA%97&c=1&src=0&wd2=&pn=0&sug=0&l=5&b=(6363475.220000001,2248539.88;16849235.22,7090011.88)&from=webmap&biz_forward={%22scaler%22:1,%22styles%22:%22pl%22}&sug_forward=&auth=xG49aFzQfWWPRGDeYBSL91PwWBvGNMKQuxHHBNRHBHVtComRB199Ay1uVt1GgvPUDZYOYIZuVt1cv3uVtGccZcuVtPWv3GuHtYAmk5b7kzC1FILPRVX8ycEWe1GD8zv7ucvY1SGpuxVthgW1aDeuEztghxehwzJJDP6GDJ4vtx77IXHxcc%40AE&device_ratio=1&tn=B_NORMAL_MAP&nn=0&u_loc=12535262,3089832&ie=utf-8&t=1553785352116',
    # '凯悦酒店':'https://map.baidu.com/?newmap=1&reqflag=pcmap&biz=1&from=webmap&da_par=direct&pcevaname=pc4.1&qt=s&da_src=searchBox.button&wd=%E5%87%AF%E6%82%A6%E9%85%92%E5%BA%97&c=1&src=0&wd2=&pn=0&sug=0&l=5&b=(6363475.220000001,2248539.88;16849235.22,7090011.88)&from=webmap&biz_forward={%22scaler%22:1,%22styles%22:%22pl%22}&sug_forward=&auth=xG49aFzQfWWPRGDeYBSL91PwWBvGNMKQuxHHBNRHBRBtzljPyBYYxy1uVt1GgvPUDZYOYIZuVt1cv3uVtGccZcuVtPWv3GuHtYAmk5b7kzC1FILPRVX8ycEWe1GD8zv7u%40ZPuVteuELtjlBhlADMMGS7JGM5ztx77IZHiCbJXLwB13AEjjg2K&device_ratio=1&tn=B_NORMAL_MAP&nn=0&u_loc=12535262,3089832&ie=utf-8&t=1553785383736',
    # '万达广场':'https://map.baidu.com/?newmap=1&reqflag=pcmap&biz=1&from=webmap&da_par=direct&pcevaname=pc4.1&qt=con&contp=0&wd=%E4%B8%87%E8%BE%BE%E5%B9%BF%E5%9C%BA&pn=0&c=1&src=3&auth=xG49aFzQfWWPRGDeYBSL91PwWBvGNMKQuxHHBNRHLzEtxjhNwzWWvy1uVt1GgvPUDZYOYIZuVt1cv3uVtGccZcuVtPWv3GuRt9DpnSeYnCEGHKNRTXZ%40BcEWe1GD8zv7u%40ZPuTtmDSOC0A%3DH73uzC1yprGnrFHQQKW9NKQUEtx77IKgHBggc1Ga&device_ratio=1&tn=B_NORMAL_MAP&nn=0&u_loc=12535262,3089832&ie=utf-8&l=11&t=1553785626170',
    # '华润置地广场':'https://map.baidu.com/?newmap=1&reqflag=pcmap&biz=1&from=webmap&da_par=direct&pcevaname=pc4.1&qt=con&contp=0&wd=%E5%8D%8E%E6%B6%A6%E7%BD%AE%E5%9C%B0%E5%B9%BF%E5%9C%BA&pn=0&c=1&src=3&auth=xG49aFzQfWWPRGDeYBSL91PwWBvGNMKQuxHHBNRHHRBthBaIWKvADzwi04vy77uy1uVt1GgvPUDZYOYIZuVt1cv3uVtGccZcuVtPWv3GuRt9DpnSeYnCEGHKNRTXZ%40BcEWe1GD8zv7u%40ZPuLtjA5Gz0iyfixA3315T213Nwtx77IeHAffbD9&device_ratio=1&tn=B_NORMAL_MAP&nn=0&u_loc=12535262,3089832&ie=utf-8&l=18&t=1553785587520',
    # '优衣库':'https://map.baidu.com/?newmap=1&reqflag=pcmap&biz=1&from=webmap&da_par=direct&pcevaname=pc4.1&qt=s&da_src=searchBox.button&wd=%E4%BC%98%E8%A1%A3%E5%BA%93&c=1&src=0&wd2=&pn=0&sug=0&l=5&b=(6363475.220000001,2248539.88;16849235.22,7090011.88)&from=webmap&biz_forward={%22scaler%22:1,%22styles%22:%22pl%22}&sug_forward=&auth=xG49aFzQfWWPRGDeYBSL91PwWBvGNMKQuxHHBNRHNzztwi04vy77ucvY1SGpuztAFwWv1GgvPUDZYOYIZuVt1cv3uVtGccZcuVtPWv3GuRt9DpnSeYnCEGHKNRTXZ%40BcEWe1GD8zv7u%40ZPuxBtqGV%40FlnDjnCENNHTXKHNRBtx77IKKHC00dE2I&device_ratio=1&tn=B_NORMAL_MAP&nn=0&u_loc=12535262,3089832&ie=utf-8&t=1553785725249',
    # 'ZARA':'https://map.baidu.com/?newmap=1&reqflag=pcmap&biz=1&from=webmap&da_par=direct&pcevaname=pc4.1&qt=s&da_src=searchBox.button&wd=ZARA&c=1&src=0&wd2=&pn=0&sug=0&l=5&b=(6363475.220000001,2248539.88;16849235.22,7090011.88)&from=webmap&biz_forward={%22scaler%22:1,%22styles%22:%22pl%22}&sug_forward=&auth=xG49aFzQfWWPRGDeYBSL91PwWBvGNMKQuxHHBNRHNHHtComRB199Ay1uVt1GgvPUDZYOYIZuVt1cv3uVtGccZcuVtPWv3GuRt9DpnSeYnCEGHKNRTXZ%40BcEWe1GD8zv7u%40ZPuxBtqGX3FprGnrFHQQKW9NKQUEtx77IKMHnGg4%40PBFHNEEjjg2JK&device_ratio=1&tn=B_NORMAL_MAP&nn=0&u_loc=12535262,3089832&ie=utf-8&t=1553785758637',
    # 'H&M':'https://map.baidu.com/?newmap=1&reqflag=pcmap&biz=1&from=webmap&da_par=direct&pcevaname=pc4.1&qt=s&da_src=searchBox.button&wd=H%26M&c=1&src=0&wd2=&pn=0&sug=0&l=5&b=(6363475.220000001,2248539.88;16849235.22,7090011.88)&from=webmap&biz_forward={%22scaler%22:1,%22styles%22:%22pl%22}&sug_forward=&auth=xG49aFzQfWWPRGDeYBSL91PwWBvGNMKQuxHHBNRHNRHtwi04vy77uy1uVt1GgvPUDZYOYIZuVt1cv3uVtGccZcuVtPWv3GuRt9DpnSeYnCEGHKNRTXZ%40BcEWe1GD8zv7u%40ZPuxBto20N%3D5CGIIFoE7T1tvJrvIKTTNZbQNTXHtx77IKNH1iifGI3&device_ratio=1&tn=B_NORMAL_MAP&nn=0&u_loc=12535262,3089832&ie=utf-8&t=1553785787001',
    # 'Gap': 'https://map.baidu.com/?newmap=1&reqflag=pcmap&biz=1&from=webmap&da_par=direct&pcevaname=pc4.1&qt=s&da_src=searchBox.button&wd=Gap&c=1&src=0&wd2=&pn=0&sug=0&l=5&b=(6363475.220000001,2248539.88;16849235.22,7090011.88)&from=webmap&biz_forward={%22scaler%22:1,%22styles%22:%22pl%22}&sug_forward=&auth=xG49aFzQfWWPRGDeYBSL91PwWBvGNMKQuxHHBNRHRNNtykiOxAXXwy1uVt1GgvPUDZYOYIZuVt1cv3uVtGccZcuVtPWv3GuTt%401qo6f8oDF2ILOSUY9%3DCcEWe1GD8zv7u%40ZPuxBtqG%40dFcvY1SGpuxztprGnrFHQQKW9NKQUEtx77IKQHEjjg2JK&device_ratio=1&tn=B_NORMAL_MAP&nn=0&u_loc=12535262,3089832&ie=utf-8&t=1553785880039',
    # 'MANGO':'https://map.baidu.com/?newmap=1&reqflag=pcmap&biz=1&from=webmap&da_par=direct&pcevaname=pc4.1&qt=s&da_src=searchBox.button&wd=MANGO&c=1&src=0&wd2=&pn=0&sug=0&l=5&b=(6363475.220000001,2248539.88;16849235.22,7090011.88)&from=webmap&biz_forward={%22scaler%22:1,%22styles%22:%22pl%22}&sug_forward=&auth=xG49aFzQfWWPRGDeYBSL91PwWBvGNMKQuxHHBNRHTVNtBnlQADZZzy1uVt1GgvPUDZYOYIZuVt1cv3uVtGccZcuVtPWv3GuTt%401qo6f8oDF2ILOSUY9%3DClEeLZNz18DaDVcCEB8zv7u%40ZPuxBtqG%40OFhjzgjyBKKEQUHEKOxtx77IKTHFkk0H3L&device_ratio=1&tn=B_NORMAL_MAP&nn=0&u_loc=12535262,3089832&ie=utf-8&t=1553785910163',
    # '李宁':'https://map.baidu.com/?newmap=1&reqflag=pcmap&biz=1&from=webmap&da_par=direct&pcevaname=pc4.1&qt=s&da_src=searchBox.button&wd=%E6%9D%8E%E5%AE%81&c=1&src=0&wd2=&pn=0&sug=0&l=5&b=(6363475.220000001,2248539.88;16849235.22,7090011.88)&from=webmap&biz_forward={%22scaler%22:1,%22styles%22:%22pl%22}&sug_forward=&auth=xG49aFzQfWWPRGDeYBSL91PwWBvGNMKQuxHHBNRHTBEtBnlQADZZzy1uVtcvY1SGpuBtGIiyRWF%3D9Q9K%3DxXw1cv3uVtGccZcuVtPWv3GuTt%401qo6f8oDF2ILOSUY9%3DCcEWe1GD8zv7u%40ZPuxBtqG%40%40FlnDjnCENNHTXKHNRBtx77IKXHGllhIKM&device_ratio=1&tn=B_NORMAL_MAP&nn=0&u_loc=12535262,3089832&ie=utf-8&t=1553785936185',
    # '耐克':'https://map.baidu.com/?newmap=1&reqflag=pcmap&biz=1&from=webmap&da_par=direct&pcevaname=pc4.1&qt=s&da_src=searchBox.button&wd=%E8%80%90%E5%85%8B&c=1&src=0&wd2=&pn=0&sug=0&l=5&b=(6363475.220000001,2248539.88;16849235.22,7090011.88)&from=webmap&biz_forward={%22scaler%22:1,%22styles%22:%22pl%22}&sug_forward=&auth=xG49aFzQfWWPRGDeYBSL91PwWBvGNMKQuxHHBNRHTNztDpnSCE%40%40By1uVt1GgvPUDZYOYIZuVt1cv3uVtGccZcuVtPWv3GuTtk1dK84yDUCZComRdXmB1F234Q6W89AcEWe1GD8zv7u%40ZPuxBtqGbLFqs2osGIRRLX%40OLRVFtx77IKZH2mmiJL4&device_ratio=1&tn=B_NORMAL_MAP&nn=0&u_loc=12535262,3089832&ie=utf-8&t=1553785975588',
    # '迪卡侬':'https://map.baidu.com/?newmap=1&reqflag=pcmap&biz=1&from=webmap&da_par=direct&pcevaname=pc4.1&qt=s&da_src=searchBox.button&wd=%E8%BF%AA%E5%8D%A1%E4%BE%AC&c=1&src=0&wd2=&pn=0&sug=0&l=5&b=(6363475.220000001,2248539.88;16849235.22,7090011.88)&from=webmap&biz_forward={%22scaler%22:1,%22styles%22:%22pl%22}&sug_forward=&auth=xG49aFzQfWWPRGDeYBSL91PwWBvGNMKQuxHHBNRHTTEtykiOxAXXwy1uVt1GgvPUDZYOYIZuVt1cv3uVtGccZcuVtPWv3GuTt%401qo6f8oDF2ILOSUY9%3DCcEWe1GD8zv7u%40ZPuxBtqGb%40FtKlReTG3MNJprGnrFHQQKW9NKQUEtx77IKbHHnnj3MN&device_ratio=1&tn=B_NORMAL_MAP&nn=0&u_loc=12535262,3089832&ie=utf-8&t=1553785998295',
    # '沃尔玛':'https://map.baidu.com/?newmap=1&reqflag=pcmap&biz=1&from=webmap&da_par=direct&pcevaname=pc4.1&qt=s&da_src=searchBox.button&wd=%E6%B2%83%E5%B0%94%E7%8E%9B&c=1&src=0&wd2=&pn=0&sug=0&l=5&b=(6363475.220000001,2248539.88;16849235.22,7090011.88)&from=webmap&biz_forward={%22scaler%22:1,%22styles%22:%22pl%22}&sug_forward=&auth=xG49aFzQfWWPRGDeYBSL91PwWBvGNMKQuxHHBNRLVxNtjDc3YMxCEBwi04vy77uy1uVt1GgvPUDZYOYIZuVt1cv3uVtGccZcuVtPWv3GuTt%401qo6f8oDF2ILOSUY9%3DCcEWe1GD8zv7u%40ZPuxBtqGbbFwyLuyK4775%3De657Z3tx77IKeHIookK4O&device_ratio=1&tn=B_NORMAL_MAP&nn=0&u_loc=12535262,3089832&ie=utf-8&t=1553786020559',
    # '永辉超市':'https://map.baidu.com/?newmap=1&reqflag=pcmap&biz=1&from=webmap&da_par=direct&pcevaname=pc4.1&qt=s&da_src=searchBox.button&wd=%E6%B0%B8%E8%BE%89%E8%B6%85%E5%B8%82&c=1&src=0&wd2=&pn=0&sug=0&l=5&b=(6363475.220000001,2248539.88;16849235.22,7090011.88)&from=webmap&biz_forward={%22scaler%22:1,%22styles%22:%22pl%22}&sug_forward=&auth=xG49aFzQfWWPRGDeYBSL91PwWBvGNMKQuxHHBNRLVNHtykiOxAXXwy1uVt1GgvPUDZYOYIZuVt1cv3uVtGccZcuVtPWv3GuTt%401qo6f8oDF2ILOSUY9%3DCcEWe1GD8zv7ucvY1SGpuxVthgW1GJDqGIdVFjlBhlADMMGS7JGM5ztx77IMgHrZZWuxz&device_ratio=1&tn=B_NORMAL_MAP&nn=0&u_loc=12535262,3089832&ie=utf-8&t=1553786077489',
    # '家乐福':'https://map.baidu.com/?newmap=1&reqflag=pcmap&biz=1&from=webmap&da_par=direct&pcevaname=pc4.1&qt=s&da_src=searchBox.button&wd=%E5%AE%B6%E4%B9%90%E7%A6%8F&c=1&src=0&wd2=&pn=0&sug=0&l=5&b=(6363475.220000001,2248539.88;16849235.22,7090011.88)&from=webmap&biz_forward={%22scaler%22:1,%22styles%22:%22pl%22}&sug_forward=&auth=xG49aFzQfWWPRGDeYBSL91PwWBvGNMKQuxHHBNRLxBztBnlQADZZzy1uVt1GgvPUDZYOYIZuVt1cv3uVtGccZcuVtPWv3GuTt%401qo6f8oDF2ILOSUY9%3DCcEWe1GD8zv7ucvY1SGpuxVthgW1GJDqGIIOFrtHpt2JSSMY%3DPMS7Gtx77IMMHt%40%40YwzB&device_ratio=1&tn=B_NORMAL_MAP&nn=0&u_loc=12535262,3089832&ie=utf-8&t=1553786135169',
    # '711便利店':'https://map.baidu.com/?newmap=1&reqflag=pcmap&biz=1&from=webmap&da_par=direct&pcevaname=pc4.1&qt=s&da_src=searchBox.button&wd=711%E4%BE%BF%E5%88%A9%E5%BA%97&c=1&src=0&wd2=&pn=0&sug=0&l=5&b=(6363475.220000001,2248539.88;16849235.22,7090011.88)&from=webmap&biz_forward={%22scaler%22:1,%22styles%22:%22pl%22}&sug_forward=&auth=xG49aFzQfWWPRGDeYBSL91PwWBvGNMKQuxHHBNRLxHNtzljPyBYYxy1uVt1GgvPUDZYOYIZuVt1cv3uVtcvY1SGpuHt300b0z8yPWv3GuxVt%3DErpTgZp1GHJMP6V8%40aDcEWe1GD8zv7u%40ZPuxBtqGII%40FvxKtx3MVVP%40dSPV8Jtx77IMNHu%3D%3D8xAC&device_ratio=1&tn=B_NORMAL_MAP&nn=0&u_loc=12535262,3089832&ie=utf-8&t=1553786158967',
}


# wbk = xlwt.Workbook()
# sheet = wbk.add_sheet('sheet 1')
# sheet.write(0, 1, 'test')  # 第0行第一列写入内容
# wbk.save('all.xls')


def sss(a, url):
    html = requests.post(url)
    # info = json.loads(eval("u" + "\'" + html.text + "\'"))
    info = json.loads(html.text)
    rb = xlrd.open_workbook('all.xls', formatting_info=True)
    # make a copy of it
    wb = xl_copy(rb)
    sheet = wb.add_sheet(a)  # 在打开的excel中添加一个sheet
    n = 0

    for i in range(len(info['more_city'])):
        sheet.write(i, 0, info['more_city'][i]['province'])
        sheet.write(i, 1, info['more_city'][i]['num'])
        n += 1
    n += 1

    for i in info['content']:
        sheet.write(n, 0, i['name'])
        sheet.write(n, 1, i['num'])
        n += 1
    n += 1
    for i in range(len(info['more_city'])):
        print(info['more_city'][i]['province'], info['more_city'][i]['num'])
        sheet.write(n, 0, info['more_city'][i]['province'])
        sheet.write(n, 1, info['more_city'][i]['num'])
        n += 1
        for j in info['more_city'][i]['city']:
            sheet.write(n, 0, j['name'])
            sheet.write(n, 1, j['num'])
            n += 1
            print('   ', end='')
            print(j['name'], j['num'])
        n += 1
        print('\n')
    wb.save('all.xls')


for u in urls:
    sss(u, urls[u])
