import requests
import time
import re
import random
from bs4 import BeautifulSoup

urlRefer = 'https://www.baidu.com/s?wd=%E8%BF%BD%E5%AF%BB%E8%87%AA%E6%88%91%E7%9A%84%E6%97%85%E9%80%94'
referer = 'http://blog.sina.com.cn/s/blog_496b2a650102wk8z.html?tj=1'
url = ['http://comet.blog.sina.com.cn/api?maintype=hits&act=4&aid=1545beda90102x6mj&ref=&varname=requestId_39097026',
       'http://comet.blog.sina.com.cn/api?maintype=hits&act=4&aid=1545beda90102wp01&ref={}&varname=requestId_9642598'.format(
           urlRefer),
       ]
headers = {
    'Referer': referer
}
referers = []


def referer():
    url = 'http://blog.sina.com.cn/lm/iframe/top/alltop_more_new_1.html'
    wb_date = requests.get(url)
    soup = BeautifulSoup(wb_date.text, 'lxml')
    urls = soup.select('td.link335bbd a')
    for url in urls:
        referers.append(url.get('href'))


def view():
    b = 0
    while True:
        time.sleep(0.7)
        wb_date = requests.get(url[0], headers=headers)
        print(wb_date.text)
        # views = re.findall('\d{4,6}', wb_date.text)
        # a = int(views[1])
        # if (a == b):
        #     time.sleep(5)
        # else:
        #     print(a)
        # b = a
        #


# referer()
view()
