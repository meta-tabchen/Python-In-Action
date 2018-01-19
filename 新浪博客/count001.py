import requests
import time
import re

url = 'http://comet.blog.sina.com.cn/api?maintype=hits&act=4&aid=5c47219b01011oox&ref=http%3A%2F%2Fblog.sina.com.cn%2Fu%2F1548165531&varname=requestId_63901005'
headers = {
    'Referer': 'http://blog.sina.com.cn/u/5874775575'
}

while True:
    wb_date = requests.get(url, headers=headers)
    a = wb_date.text.split('=')[-1]
    a = int(re.findall('\d{1,10}', a)[0])
    time.sleep(10)
    wb_date = requests.get(url, headers=headers)
    b = wb_date.text.split('=')[-1]
    b = int(re.findall('\d{1,10}', b)[0])
    print((b - a) * 6 * 60)
