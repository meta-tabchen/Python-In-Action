from multiprocessing import Pool
import requests
import pymongo
import random
import time
from string import punctuation

client = pymongo.MongoClient('localhost', 27017)
proxy = client['proxy']
good = proxy['good']
raw = proxy['raw']
all = proxy['all']


def getPort():
    proxy_list = [x['ip'].split(':')[-1] for x in good.find()]
    alls = set(proxy_list)
    allcounts = []
    for one in alls:
        allcounts.append({'port': one, 'count': proxy_list.count(one)})
    allcounts = sorted(allcounts, key=lambda x: x['count'], reverse=True)
    for i in allcounts:
        print(i)


def getIpAdress():
    proxy_list = [x['ip'].split('.')[0] +'.'+ x['ip'].split('.')[1] for x in good.find()]
    alls = set(proxy_list)
    allcounts = []
    for one in alls:
        allcounts.append({'ip': one, 'count': proxy_list.count(one)})
    allcounts = sorted(allcounts, key=lambda x: x['count'], reverse=True)
    for i in allcounts:
        print(i)
def getHelp():
    proxy_list = [x['ip'] for x in good.find()]
    for i in proxy_list:
        if '94.177' in i:
            print(i)
# getIpAdress()
getHelp()