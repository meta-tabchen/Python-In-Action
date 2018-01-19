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

proxy_list = [x['ip'] for x in good.find()]


# 2、西刺的网页
def ip002(i):
    #nn:2041 wn:368 nt:495 wt:1395
    # names = ['wn','nt', 'wt',  'nn']
    names = ['nn']
    for name in names:
        i = 'http://www.xicidaili.com/{}/{}'.format(name, str(i))
        getXiCiIp(i)


def getXiCiIp(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'
        }
        ip = random.choice(proxy_list)
        ip = "http://{}".format(ip)
        proxies = {'http': ip}
        wb_data = requests.get(url, headers=headers, proxies=proxies)
        soup = BeautifulSoup(wb_data.text, 'lxml')
        ips = soup.select('.odd > td:nth-of-type(2)')
        ports = soup.select('.odd > td:nth-of-type(3)')
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
    pool.map(ip002, range(500))
