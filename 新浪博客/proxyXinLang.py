import requests
import random
import re
import pymongo
import time
from multiprocessing import Pool

client = pymongo.MongoClient('localhost', 27017)
proxy = client['proxy']
good = proxy['good']
payGood = proxy['payGood']

proxy_list = [x['ip'] for x in good.find()]
baidu = 'https://www.baidu.com/s?wd=%E8%BF%BD%E5%AF%BB%E8%87%AA%E6%88%91%E7%9A%84%E6%97%85%E9%80%94&rsv_spt=1&rsv_iqid=0xa6a84d180000dcd0&issp=1&f=8&rsv_bp=0&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_sug3=19&rsv_sug1=10&rsv_sug7=100&rsv_sug2=0&inputT=5326&rsv_sug4=5326&rsv_sug=2'
referers = ['http://blog.sina.com.cn/u/1300871220', 'http://blog.sina.com.cn/u/1300871220',
            'http://blog.sina.com.cn/u/1216826604', 'http://blog.sina.com.cn/u/1216826604',
            'http://blog.sina.com.cn/u/1245296155', 'http://blog.sina.com.cn/u/1245296155',
            'http://blog.sina.com.cn/u/1284139322', 'http://blog.sina.com.cn/u/1284139322',
            'http://blog.sina.com.cn/u/1285707277', 'http://blog.sina.com.cn/u/1285707277',
            'http://blog.sina.com.cn/u/1458594614', 'http://blog.sina.com.cn/u/1458594614',
            'http://blog.sina.com.cn/u/1236135807', 'http://blog.sina.com.cn/u/1236135807',
            'http://blog.sina.com.cn/u/1191258123', 'http://blog.sina.com.cn/u/1191258123',
            'http://blog.sina.com.cn/u/1504965870', 'http://blog.sina.com.cn/u/1504965870',
            'http://blog.sina.com.cn/u/1220824437', 'http://blog.sina.com.cn/u/1220824437',
            'http://blog.sina.com.cn/u/1292400222', 'http://blog.sina.com.cn/u/1292400222',
            'http://blog.sina.com.cn/u/1298535315', 'http://blog.sina.com.cn/u/1298535315',
            'http://blog.sina.com.cn/u/1279884602', 'http://blog.sina.com.cn/u/1279884602',
            'http://blog.sina.com.cn/u/1364334665', 'http://blog.sina.com.cn/u/1364334665',
            'http://blog.sina.com.cn/u/1254470047', 'http://blog.sina.com.cn/u/1254470047',
            'http://blog.sina.com.cn/u/1189591617', 'http://blog.sina.com.cn/u/1189591617',
            'http://blog.sina.com.cn/u/1190363061', 'http://blog.sina.com.cn/u/1190363061',
            'http://blog.sina.com.cn/u/1246792191', 'http://blog.sina.com.cn/u/1246792191',
            'http://blog.sina.com.cn/u/1347712670', 'http://blog.sina.com.cn/u/1347712670',
            'http://blog.sina.com.cn/u/1265722751', 'http://blog.sina.com.cn/u/1265722751',
            'http://blog.sina.com.cn/u/1145642397', 'http://blog.sina.com.cn/u/1145642397',
            'http://blog.sina.com.cn/u/1278228085', 'http://blog.sina.com.cn/u/1278228085',
            'http://blog.sina.com.cn/u/1233526741', 'http://blog.sina.com.cn/u/1233526741',
            'http://blog.sina.com.cn/u/1243037810', 'http://blog.sina.com.cn/u/1243037810',
            'http://blog.sina.com.cn/u/1319231304', 'http://blog.sina.com.cn/u/1319231304',
            'http://blog.sina.com.cn/u/1456252804', 'http://blog.sina.com.cn/u/1456252804',
            'http://blog.sina.com.cn/u/1225899402', 'http://blog.sina.com.cn/u/1225899402',
            'http://blog.sina.com.cn/u/1243881594', 'http://blog.sina.com.cn/u/1243881594',
            'http://blog.sina.com.cn/u/1420174783', 'http://blog.sina.com.cn/u/1420174783',
            'http://blog.sina.com.cn/u/1364616083', 'http://blog.sina.com.cn/u/1364616083',
            'http://blog.sina.com.cn/u/1282871591', 'http://blog.sina.com.cn/u/1282871591',
            'http://blog.sina.com.cn/u/1233227211', 'http://blog.sina.com.cn/u/1233227211',
            'http://blog.sina.com.cn/u/1191211465', 'http://blog.sina.com.cn/u/1191211465',
            'http://blog.sina.com.cn/u/1197950454', 'http://blog.sina.com.cn/u/1197950454',
            'http://blog.sina.com.cn/u/1223299212', 'http://blog.sina.com.cn/u/1223299212',
            'http://blog.sina.com.cn/u/1279916282', 'http://blog.sina.com.cn/u/1279916282',
            'http://blog.sina.com.cn/u/1266020172', 'http://blog.sina.com.cn/u/1266020172',
            'http://blog.sina.com.cn/u/1188552450', 'http://blog.sina.com.cn/u/1188552450',
            'http://blog.sina.com.cn/u/1368179347', 'http://blog.sina.com.cn/u/1368179347',
            'http://blog.sina.com.cn/u/1096536995', 'http://blog.sina.com.cn/u/1096536995',
            'http://blog.sina.com.cn/u/1228293531', 'http://blog.sina.com.cn/u/1228293531',
            'http://blog.sina.com.cn/u/1223841312', 'http://blog.sina.com.cn/u/1223841312',
            'http://blog.sina.com.cn/u/1319802272', 'http://blog.sina.com.cn/u/1319802272',
            'http://blog.sina.com.cn/u/1420555367', 'http://blog.sina.com.cn/u/1420555367',
            'http://blog.sina.com.cn/u/1481028245', 'http://blog.sina.com.cn/u/1481028245',
            'http://blog.sina.com.cn/u/1288557173', 'http://blog.sina.com.cn/u/1288557173',
            'http://blog.sina.com.cn/u/1257495952', 'http://blog.sina.com.cn/u/1257495952',
            'http://blog.sina.com.cn/u/1215172700', 'http://blog.sina.com.cn/u/1215172700',
            'http://blog.sina.com.cn/u/1633662514', 'http://blog.sina.com.cn/u/1633662514',
            'http://blog.sina.com.cn/u/1305431810', 'http://blog.sina.com.cn/u/1305431810',
            'http://blog.sina.com.cn/u/1414660444', 'http://blog.sina.com.cn/u/1414660444',
            'http://blog.sina.com.cn/u/1198251274', 'http://blog.sina.com.cn/u/1198251274',
            'http://blog.sina.com.cn/u/1025708803', 'http://blog.sina.com.cn/u/1025708803',
            'http://blog.sina.com.cn/u/1236617023', 'http://blog.sina.com.cn/u/1236617023',
            'http://blog.sina.com.cn/u/1189615035', 'http://blog.sina.com.cn/u/1189615035',
            'http://blog.sina.com.cn/u/1249424622', 'http://blog.sina.com.cn/u/1249424622',
            'http://blog.sina.com.cn/u/1494856974', 'http://blog.sina.com.cn/u/1494856974',
            'http://blog.sina.com.cn/u/1192230491', 'http://blog.sina.com.cn/u/1192230491',
            'http://blog.sina.com.cn/u/1258205462', 'http://blog.sina.com.cn/u/1258205462',
            'http://blog.sina.com.cn/u/1248272901', 'http://blog.sina.com.cn/u/1248272901',
            'http://blog.sina.com.cn/u/1213332190', 'http://blog.sina.com.cn/u/1213332190',
            'http://blog.sina.com.cn/u/1320219435', 'http://blog.sina.com.cn/u/1320219435',
            'http://blog.sina.com.cn/u/1336750060', 'http://blog.sina.com.cn/u/1336750060',
            'http://blog.sina.com.cn/u/1272933544', 'http://blog.sina.com.cn/u/1272933544',
            'http://blog.sina.com.cn/u/1286664381', 'http://blog.sina.com.cn/u/1286664381',
            'http://blog.sina.com.cn/u/1033436027', 'http://blog.sina.com.cn/u/1033436027',
            'http://blog.sina.com.cn/u/1307309734', 'http://blog.sina.com.cn/u/1307309734',
            'http://blog.sina.com.cn/u/1346553137', 'http://blog.sina.com.cn/u/1346553137',
            'http://blog.sina.com.cn/u/1246151574', 'http://blog.sina.com.cn/u/1246151574',
            'http://blog.sina.com.cn/u/1571875947', 'http://blog.sina.com.cn/u/1571875947',
            'http://blog.sina.com.cn/u/1199712261', 'http://blog.sina.com.cn/u/1199712261',
            'http://blog.sina.com.cn/u/1419092951', 'http://blog.sina.com.cn/u/1419092951',
            'http://blog.sina.com.cn/u/1569548481', 'http://blog.sina.com.cn/u/1569548481',
            'http://blog.sina.com.cn/u/1270344441', 'http://blog.sina.com.cn/u/1270344441',
            'http://blog.sina.com.cn/u/1302676937', 'http://blog.sina.com.cn/u/1302676937',
            'http://blog.sina.com.cn/u/1354128900', 'http://blog.sina.com.cn/u/1354128900',
            'http://blog.sina.com.cn/u/1345654037', 'http://blog.sina.com.cn/u/1345654037',
            'http://blog.sina.com.cn/u/1289997621', 'http://blog.sina.com.cn/u/1289997621',
            'http://blog.sina.com.cn/u/1639802725', 'http://blog.sina.com.cn/u/1639802725',
            'http://blog.sina.com.cn/u/1249159055', 'http://blog.sina.com.cn/u/1249159055',
            'http://blog.sina.com.cn/u/1362607654', 'http://blog.sina.com.cn/u/1362607654',
            'http://blog.sina.com.cn/u/1195201334', 'http://blog.sina.com.cn/u/1195201334',
            'http://blog.sina.com.cn/u/1396812534', 'http://blog.sina.com.cn/u/1396812534',
            'http://blog.sina.com.cn/u/1338707944', 'http://blog.sina.com.cn/u/1338707944',
            'http://blog.sina.com.cn/u/1224361860', 'http://blog.sina.com.cn/u/1224361860',
            'http://blog.sina.com.cn/u/1198920804', 'http://blog.sina.com.cn/u/1198920804',
            'http://blog.sina.com.cn/u/1195403385', 'http://blog.sina.com.cn/u/1195403385',
            'http://blog.sina.com.cn/u/1288109750', 'http://blog.sina.com.cn/u/1288109750',
            'http://blog.sina.com.cn/u/1210558317', 'http://blog.sina.com.cn/u/1210558317',
            'http://blog.sina.com.cn/u/1299345257', 'http://blog.sina.com.cn/u/1299345257',
            'http://blog.sina.com.cn/u/1236937620', 'http://blog.sina.com.cn/u/1236937620',
            'http://blog.sina.com.cn/u/1253531973', 'http://blog.sina.com.cn/u/1253531973',
            'http://blog.sina.com.cn/u/1156966391', 'http://blog.sina.com.cn/u/1156966391',
            'http://blog.sina.com.cn/u/1285846970', 'http://blog.sina.com.cn/u/1285846970',
            'http://blog.sina.com.cn/u/1198367585', 'http://blog.sina.com.cn/u/1198367585',
            'http://blog.sina.com.cn/u/1514551012', 'http://blog.sina.com.cn/u/1514551012',
            'http://blog.sina.com.cn/u/1223537940', 'http://blog.sina.com.cn/u/1223537940',
            'http://blog.sina.com.cn/u/1195031270', 'http://blog.sina.com.cn/u/1195031270',
            'http://blog.sina.com.cn/u/1278127565', 'http://blog.sina.com.cn/u/1278127565',
            'http://blog.sina.com.cn/u/1288814951', 'http://blog.sina.com.cn/u/1288814951']


def getUrl(referer):
    url = [
        'http://comet.blog.sina.com.cn/api?maintype=hits&act=4&aid=1545beda90102wj99&ref={}&varname=requestId_8163105',
        'http://comet.blog.sina.com.cn/api?maintype=hits&act=4&aid=1545beda90102wjqa&ref={}&varname=requestId_8640991',
        'http://comet.blog.sina.com.cn/api?maintype=hits&act=4&aid=1545beda90102wjq9&ref={}&varname=requestId_2160121',
        'http://comet.blog.sina.com.cn/api?maintype=hits&act=4&aid=1545beda90102wj4v&ref={}&varname=requestId_9480556',
        'http://comet.blog.sina.com.cn/api?maintype=hits&act=4&aid=1545beda90102wj4r&ref={}&varname=requestId_7481746',
        'http://comet.blog.sina.com.cn/api?maintype=hits&act=4&aid=1545beda90102wj4t&ref={}&varname=requestId_8701622',
        'http://comet.blog.sina.com.cn/api?maintype=hits&act=4&aid=1545beda90102wiwm&ref={}&varname=requestId_7082901',
        'http://comet.blog.sina.com.cn/api?maintype=hits&act=4&aid=1545beda90102wj4r&ref={}&varname=requestId_8221396',
        'http://comet.blog.sina.com.cn/api?maintype=hits&act=4&aid=1545beda90102wj2o&ref={}&varname=requestId_8580399',
        'http://comet.blog.sina.com.cn/api?maintype=hits&act=4&aid=1545beda90102wizs&ref={}&varname=requestId_1291354',
        'http://comet.blog.sina.com.cn/api?maintype=hits&act=4&aid=1545beda90102wjhc&ref={}&varname=requestId_4253049',
        'http://comet.blog.sina.com.cn/api?maintype=hits&act=4&aid=1545beda90102wirr&ref={}&varname=requestId_6294629',
        'http://comet.blog.sina.com.cn/api?maintype=hits&act=4&aid=1545beda90102wj71&ref={}&varname=requestId_3261146',
        'http://comet.blog.sina.com.cn/api?maintype=hits&act=4&aid=1545beda90102wiwm&ref={}&varname=requestId_1994092',
        'http://comet.blog.sina.com.cn/api?maintype=hits&act=4&aid=1545beda90102wivu&ref={}&varname=requestId_5618386',
        'http://comet.blog.sina.com.cn/api?maintype=hits&act=4&aid=1545beda90102wj4t&ref={}&varname=requestId_6179653',
        'http://comet.blog.sina.com.cn/api?maintype=hits&act=4&aid=1545beda90102wj4w&ref={}&varname=requestId_4622845',
        'http://comet.blog.sina.com.cn/api?maintype=hits&act=4&aid=1545beda90102wj71&ref={}&varname=requestId_2595881',
        'http://comet.blog.sina.com.cn/api?maintype=hits&act=4&aid=1545beda90102wjpt&ref={}&varname=requestId_6293496',
        'http://comet.blog.sina.com.cn/api?maintype=hits&act=4&aid=1545beda90102wjq1&ref={}&varname=requestId_1661619',
        'http://comet.blog.sina.com.cn/api?maintype=hits&act=4&aid=1545beda90102wjq1&ref={}&varname=requestId_4865008',
        'http://comet.blog.sina.com.cn/api?maintype=hits&act=4&aid=1545beda90102wj4p&ref={}&varname=requestId_5367785',
        'http://comet.blog.sina.com.cn/api?maintype=hits&act=4&aid=1545beda90102wiu5&ref={}&varname=requestId_3285863',
        'http://comet.blog.sina.com.cn/api?maintype=hits&act=4&aid=1545beda90102wjpo&ref={}&varname=requestId_8236467',
        'http://comet.blog.sina.com.cn/api?maintype=hits&act=4&aid=1545beda90102wj45&ref={}&varname=requestId_4982688',
        'http://comet.blog.sina.com.cn/api?maintype=hits&act=4&aid=1545beda90102wj4w&ref={}&varname=requestId_8541361',
        'http://comet.blog.sina.com.cn/api?maintype=hits&act=4&aid=1545beda90102wj73&ref={}&varname=requestId_3421371',
        'http://comet.blog.sina.com.cn/api?maintype=hits&act=4&aid=1545beda90102wirr&ref={}&varname=requestId_5978978',
        'http://comet.blog.sina.com.cn/api?maintype=hits&act=4&aid=1545beda90102wj1v&ref={}&varname=requestId_8075896',
        'http://comet.blog.sina.com.cn/api?maintype=hits&act=4&aid=1545beda90102wj9a&ref={}&varname=requestId_6217699',
        'http://comet.blog.sina.com.cn/api?maintype=hits&act=4&aid=1545beda90102wj99&ref={}&varname=requestId_7201000',
        'http://comet.blog.sina.com.cn/api?maintype=hits&act=4&aid=1545beda90102wj4t&ref={}&varname=requestId_8652967',
        'http://comet.blog.sina.com.cn/api?maintype=hits&act=4&aid=1545beda90102wjpo&ref={}&varname=requestId_3609305',
        'http://comet.blog.sina.com.cn/api?maintype=hits&act=4&aid=1545beda90102wjq9&ref={}&varname=requestId_1743548',
        'http://comet.blog.sina.com.cn/api?maintype=hits&act=4&aid=1545beda90102wjq1&ref={}&varname=requestId_4643470',
        'http://comet.blog.sina.com.cn/api?maintype=hits&act=4&aid=1545beda90102wjq8&ref={}&varname=requestId_6334563',
        'http://comet.blog.sina.com.cn/api?maintype=hits&act=4&aid=1545beda90102wj4p&ref={}&varname=requestId_6107484',
        'http://comet.blog.sina.com.cn/api?maintype=hits&act=4&aid=1545beda90102wjhf&ref={}&varname=requestId_6759254',
        'http://comet.blog.sina.com.cn/api?maintype=hits&act=4&aid=1545beda90102wjhd&ref={}&varname=requestId_2898275',
        'http://comet.blog.sina.com.cn/api?maintype=hits&act=4&aid=1545beda90102wp01&ref={}&varname=requestId_8377588',
        'http://comet.blog.sina.com.cn/api?maintype=hits&act=4&aid=1545beda90102wp01&ref={}&varname=requestId_6303028',
        'http://comet.blog.sina.com.cn/api?maintype=hits&act=4&aid=1545beda90102wj45&ref={}&varname=requestId_3544825',
        'http://comet.blog.sina.com.cn/api?maintype=hits&act=4&aid=1545beda90102wj4w&ref={}&varname=requestId_1455306',
        'http://comet.blog.sina.com.cn/api?maintype=hits&act=4&aid=1545beda90102wjhe&ref={}&varname=requestId_4794491',
        'http://comet.blog.sina.com.cn/api?maintype=hits&act=4&aid=1545beda90102wiu5&ref={}&varname=requestId_5234721',
        'http://comet.blog.sina.com.cn/api?maintype=hits&act=4&aid=1545beda90102wiwm&ref={}&varname=requestId_7505278',
        'http://comet.blog.sina.com.cn/api?maintype=hits&act=4&aid=1545beda90102wj98&ref={}&varname=requestId_1502941',
        'http://comet.blog.sina.com.cn/api?maintype=hits&act=4&aid=1545beda90102wjhd&ref={}&varname=requestId_9839171']
    return random.choice(url).format(referer)


def getFromPay():
    good.drop()
    api = 'http://api.ip.data5u.com/api/get.shtml?order=59f3d1290512f231f0acd124242fe932&num=500&carrier=0&protocol=1&an1=1&an2=2&sp1=1&sp2=2&sp3=3&sort=1&system=1&distinct=0&rettype=1&seprator=%0A'
    wb_data = requests.get(api)
    list = wb_data.content.split()
    for ip in list:
        ip = str(ip).strip('b\'')
        good.insert_one({'ip': ip})


def view(i):
    try:
        ip = random.choice(proxy_list)
        referer = random.choice(referers)
        headers = {
            'Referer': referer,
        }
        ip = "http://{}".format(ip)
        proxies = {'http': ip}
        url = getUrl(referer)
        wb_date = requests.get(url, headers=headers, proxies=proxies)
        #print(wb_date.text)

    except:
        pass


if __name__ == '__main__':
    # while True:
    #     getFromPay()
    #     print('执行了一次，good的代理总数是', good.find().count())
    pool = Pool()
    pool = Pool(processes=150)
    pool.map(view, range(2000000))

    # print(getUrl(random.choice(referers)))
