import requests
import json
from bs4 import BeautifulSoup
url='https://s.m.taobao.com/search?q=深入理解计算机系统&n=11&m=api4h5&page=1&style=list'

wb_data=requests.get(url).json()
for item in wb_data['listItem']:
    print(item)
print(len(wb_data['listItem']))