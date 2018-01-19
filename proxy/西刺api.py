import requests
import random

url = 'http://comet.blog.sina.com.cn/api?maintype=hits&act=4&aid=1545beda90102wj70&ref=&varname=requestId_99212254'
headers = {
    'Referer': 'http://blog.sina.com.cn/s/blog_1545beda90102wj4u.html'
}
def ip001():
    name = 'free2016.txt'
    wb_data = requests.get('http://api.xicidaili.com/free2016.txt')
    list = wb_data.content.split()
    for ip in list:
        ip = str(ip).strip('b\'')
        proxies = {'http': '122.236.159.76:8118'}
        try:
            wb_date = requests.get(url, headers=headers,proxies=proxies)
            print(wb_date.text)
        except:
            pass

ip001()