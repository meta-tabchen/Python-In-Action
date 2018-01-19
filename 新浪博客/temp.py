import requests
from bs4 import BeautifulSoup
from lxml import etree
import random
import time
from multiprocessing import Pool
import pymongo

client = pymongo.MongoClient('localhost', 27017)
proxy = client['proxy']
good = proxy['good']

proxy_list = [x['ip'] for x in good.find()]

homeUrl = 'http://blog.sina.com.cn/s/articlelist_5710278057_0_1.html'


# 获取博客目录的所有的文章链接
def getArticleUrl(referers):
    rootUrl = 'http://comet.blog.sina.com.cn/api?maintype=hits&act=4&aid={}&ref={}&varname=requestId_{}'
    wb_data = requests.get(homeUrl)
    selsect = etree.HTML(wb_data.text)
    links = selsect.xpath('//span[@class="atc_title"]/a/@href')
    urls = []
    for referer in referers:
        link = random.choice(links)
        aid = link.split('/')[-1].split('_')[-1].split('.')[0]
        requestId = int(random.uniform(1111111, 9999999))
        url = rootUrl.format(aid, referer, str(requestId))
        urls.append(url)
    return urls


def getReferer():
    referers = []
    url = 'http://blog.sina.com.cn/lm/iframe/top/alltop_more_new_1.html'
    wb_date = requests.get(url)
    soup = BeautifulSoup(wb_date.text, 'lxml')
    urls = soup.select('td.link335bbd a')
    for url in urls:
        referers.append(url.get('href'))
    return referers


def view(i):
    try:
        referers = getReferer()
        urls = getArticleUrl(referers)
        for url, referer in zip(urls, referers):
            headers = {
                'Referer': referer
            }
            ip = random.choice(proxy_list)
            proxies = {'http': ip}

            wb_date = requests.get(url, headers=headers, proxies=proxies)
            # print(wb_date.text)
    except:
        pass

# if __name__ == '__main__':
#     pool = Pool()
#     pool = Pool(processes=100)
#     pool.map(view, range(200000))
print(proxy_list)