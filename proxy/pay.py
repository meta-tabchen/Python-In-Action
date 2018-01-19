import requests
import pymongo
import time

client = pymongo.MongoClient('localhost', 27017)
proxy = client['proxy']
pay = proxy['pay']
while True:
    time.sleep(0.5)
    wb_date = requests.get('http://api.ip.data5u.com/dynamic/get.html?order=59f3d1290512f231f0acd124242fe932&sep=2')
    pay.insert_one({'ip': wb_date.text.strip()})
    print(wb_date.text.strip())

    wb_date = requests.get('http://api.ip.data5u.com/dynamic/get.html?order=59f3d1290512f231f0acd124242fe932&sep=2')
    pay.insert_one({'ip': wb_date.text.strip()})
    print(wb_date.text.strip())
