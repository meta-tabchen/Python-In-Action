import requests
import time
import re

url = 'http://comet.blog.sina.com.cn/api?maintype=hits&act=4&aid=1545beda90102wj70&ref=&varname=requestId_99212254'
headers = {
    'Referer': 'http://blog.sina.com.cn/s/blog_1545beda90102wj4u.html'
}
b = 0
while True:
    wb_date = requests.get(url, headers=headers)
    views = re.findall('\d{7}', wb_date.text)
    # views
    a = int(views[1])

    time.sleep(60)
    wb_date = requests.get(url, headers=headers)
    views = re.findall('\d{7}', wb_date.text)
    b = int(views[1])

    print((b - a)*60)
