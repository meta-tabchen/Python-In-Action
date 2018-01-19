import threading
import time
import requests
from multiprocessing import Pool
import requests
import pymongo
import time

from bs4 import BeautifulSoup
from multiprocessing import Pool

client = pymongo.MongoClient('localhost', 27017)
proxy = client['proxy']
all = proxy['all']
raw = proxy['raw']
good = proxy['good']
pay = proxy['pay']
payGood = proxy['payGood']
help = proxy['help']


def veriIP(url, ip, type):
    try:
        help.insert_one({'op': ip})
        useIp = '{}://{}'.format(type, str(ip))
        proxy_ip = {type: useIp}
        a = time.clock()
        we_data = requests.get(url, proxies=proxy_ip)
        b = time.clock() - a
        if (we_data.status_code == 200):
            if (b < 8):
                good.insert_one({'ip': ip})
                # raw1.insert_one({'ip': ip})
            elif (b < 10):

                pass
    except:
        pass


def verHelp(ip):
    url = 'http://blog.sina.com.cn/s/blog_1545beda90102wj4u.html'

    type = 'http'
    veriIP(url, ip, type)


def getKIp(url):
    print('getKIP')
    wb_date = requests.get('http://www.kuaidaili.com/free/')
    soup = BeautifulSoup(wb_date.text, 'lxml')
    ips = soup.select('#list > table > tbody > tr > td:nth-of-type(1)')
    ports = soup.select('#list > table > tbody > tr > td:nth-of-type(2)')
    for ip, port in zip(ips, ports):
        ip = ip.get_text() + ':' + port.get_text()
        raw.insert_one({'ip': ip})


def getXiCiIp(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'
    }
    wb_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    ips = soup.select('.odd > td:nth-of-type(2)')
    ports = soup.select('.odd > td:nth-of-type(3)')
    for ip, port in zip(ips, ports):
        ip = ip.get_text() + ':' + port.get_text()
        raw.insert_one({'ip': ip})


# 1、西刺的api
def ip001():
    wb_data = requests.get('http://api.xicidaili.com/free2016.txt')
    list = wb_data.content.split()
    for ip in list:
        ip = str(ip).strip('b\'')
        raw.insert_one({'ip': ip})


# 2、西刺的网页
def ip002():
    time.sleep(2)
    # names = ['wn', 'wt', 'nt', 'nn']
    names = ['nt', 'nn']
    for name in names:
        for i in range(1, 2):
            i = 'http://www.xicidaili.com/{}/{}'.format(name, str(i))
            getXiCiIp(i)


# 3、快代理的
def ip003():
    for i in range(1, 10):
        time.sleep(1)
        names = ['inha', 'outha']
        for name in names:
            url = 'http://www.kuaidaili.com/free/{}/{}/'.format(name, i)
            wb_date = requests.get(url)
            # print(wb_date.text)
            soup = BeautifulSoup(wb_date.text, 'lxml')
            ips = soup.select('#list > table > tbody > tr > td:nth-of-type(1)')
            ports = soup.select('#list > table > tbody > tr > td:nth-of-type(2)')
            for ip, port in zip(ips, ports):
                ip = ip.get_text() + ':' + port.get_text()
                raw.insert_one({'ip': ip})


def ip004():
    url = 'http://www.xdaili.cn/ipagent//freeip/getFreeIps?page=1&rows=10'
    wb_data = requests.get(url)
    datas = wb_data.json()['rows']
    for data in datas:
        ip = data['ip'] + ':' + data['port']
        raw.insert_one({'ip': ip})


# 5、虎头代理
def ip005():
    # wb_data = requests.get('http://7085276879513359.standard.hutoudaili.com/?num=600&area_type=0&anonymity=2&order=1')
    # list = wb_data.content.split()
    # for ip in list:
    #     ip = str(ip).strip('b\'')
    #     raw.insert_one({'ip': ip})
    # time.sleep(1)

    wb_data = requests.get('http://7085276879513359.standard.hutoudaili.com/?num=2000&scheme=1&order=1')
    list = wb_data.content.split()
    for ip in list:
        ip = str(ip).strip('b\'')
        raw.insert_one({'ip': ip})
    print('从虎头代理获取结束')


def getFromPay():
    api = 'http://api.ip.data5u.com/api/get.shtml?order=59f3d1290512f231f0acd124242fe932&num=10000&carrier=0&protocol=0&an3=3&sp1=1&sp2=2&sp3=3&sort=1&distinct=0&rettype=1&seprator=%0A'
    wb_data = requests.get(api)
    list = wb_data.content.split()
    for ip in list:
        ip = str(ip).strip('b\'')
        raw.insert_one({'ip': ip})


# 从一个文件中获取
def getFromFile():
    name = 'free2016.txt'
    f = open(name, 'r')
    list = f.read().split('\n')
    for ip in list:
        # print(ip)
        raw.insert_one({'ip': ip})


def getAllIp():
    # getFromFile()
    # 1、西刺的api
    ip001()
    # 2、西刺的网页
    ip002()
    # 3、快代理的
    ip003()
    # 4、讯代理
    ip004()


# 查看重复的个数
def countNumber(name):
    temp = proxy[name]
    print('处理前', temp.find().count())
    all = set([x['ip'] for x in temp.find()])
    print('处理后', len(all))


# 去除重复的数据
def removeRepeat(name):
    countNumber(name)
    temp = proxy[name]
    all = set([x['ip'] for x in temp.find()])
    temp.drop()
    for ip in all:
        temp.insert_one({'ip': ip})
    print('去除重复完成')


# 将a中全部拷贝到b中
def copyFromTo(dA, dB):
    a = proxy[dA]
    b = proxy[dB]
    for i in a.find():
        b.insert_one({'ip': i['ip']})
    print('拷贝完成')
    removeRepeat(dB)


if __name__ == '__main__':
    # copyFromTo('raw', 'all')
    # raw.drop()
    help.drop()
    good.drop()
    # ip005()
    # getAllIp()
    # copyFromTo('raw', 'all')
    # removeRepeat('all')

    proxy_list = set([ip['ip'] for ip in all.find()])
    for ip in proxy_list:
        ti = threading.Thread(target=verHelp, args=(ip,))
        ti.start()
    print('over')
