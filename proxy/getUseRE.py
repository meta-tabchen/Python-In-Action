import re
import requests
import pymongo
import random
from multiprocessing import Pool

client = pymongo.MongoClient('localhost', 27017)
proxy = client['proxy']
all = proxy['all']
test = proxy['test']
good = proxy['good']

proxy_list = [ip['ip'] for ip in good.find()]


def get(i):
    try:
        i = i * 15
        url = 'http://proxydb.net/?offset={}'.format(i)
        pattern = '((25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[1-9])\.(25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[1-9]|0)\.(25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[1-9]|0)\.(25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[0-9])(:[0-9]{3,6}))'
        # pattern=''
        ip = random.choice(proxy_list)
        proxies = {'http': ip}
        wb_date = requests.get(url, proxies=proxies)
        allIPs = re.findall(pattern, wb_date.text)
        for ip in allIPs:
            # ip=list(ip)
            # print(ip)
            test.insert_one({'ip': ip[0]})
            print(ip)
    except:
        pass


if __name__ == '__main__':
    # test.drop()
    pool = Pool(processes=1)
    pool.map(get, range(0, 578))
