import threading
import time
import requests
from multiprocessing import Pool

url = 'http://comet.blog.sina.com.cn/api?maintype=hits&act=4&aid=5c47219b01011oox&ref=http%3A%2F%2Fblog.sina.com.cn%2Fu%2F1548165531&varname=requestId_63901005'
headers = {
    'Referer': 'http://blog.sina.com.cn/u/5874775575'
}


def view(i):
    try:
        wb_date = requests.get(url, headers=headers)
        print(wb_date.text)
    except:
        pass


def go(i):
    while True:
        for i in range(40):
            thread = threading.Thread(target=view, args=(i,))
            thread.start()


#
# if __name__ == '__main__':
#     # while True:
#     #     getFromPay()
#     #     print('执行了一次，good的代理总数是', good.find().count())
#     pool = Pool()
#     pool = Pool(processes=200)
#     pool.map(go, range(20000000))
go(9)
