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
import time
from bs4 import BeautifulSoup

url = 'http://www.kuaidaili.com'

proxy_list = [x['ip'] for x in good.find()]


def ip003(i):
    try:
        names = ['inha', 'outha', 'intr', 'outrr']
        for name in names:
            url = 'http://www.kuaidaili.com/free/{}/{}/'.format(name, i)
            ip = random.choice(proxy_list)
            ip = "http://{}".format(ip)
            proxies = {'http': ip}
            wb_date = requests.get(url,proxies=proxies)
            soup = BeautifulSoup(wb_date.text, 'lxml')
            ips = soup.select('#list > table > tbody > tr > td:nth-of-type(1)')
            ports = soup.select('#list > table > tbody > tr > td:nth-of-type(2)')
            for ip, port in zip(ips, ports):
                ip = ip.get_text() + ':' + port.get_text()
                raw.insert_one({'ip': ip})
    except:
        pass


if __name__ == '__main__':
    # while True:
    #     getFromPay()
    #     print('执行了一次，good的代理总数是', good.find().count())
    pool = Pool()
    pool = Pool(processes=100)
    pool.map(ip003, range(1600))
