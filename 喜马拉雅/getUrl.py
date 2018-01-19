from bs4 import BeautifulSoup
import pymongo
from lxml import etree
from multiprocessing import Pool
import requests
import os
import time
import threading

# 数据库的操作

'''
mport pymongo
con = pymongo.Connection('localhost', 27017)

mydb = con.mydb # new a database
mydb.add_user('test', 'test') # add a user
mydb.authenticate('test', 'test') # check auth

muser = mydb.user # new a table
 
muser.save({'id':1, 'name':'test'}) # add a record

muser.insert({'id':2, 'name':'hello'}) # add a record
muser.find_one() # find a record

muser.find_one({'id':2}) # find a record by query
 
muser.create_index('id')

muser.find().sort('id', pymongo.ASCENDING) # DESCENDING
# muser.drop() delete table
muser.find({'id':1}).count() # get records number

muser.find({'id':1}).limit(3).skip(2) # start index is 2 limit 3 records

muser.remove({'id':1}) # delet records where id = 1
 
muser.update({'id':2}, {'$set':{'name':'haha'}}) # update one recor
'''
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 '
}

client = pymongo.MongoClient('localhost', 27017)
ximalaya = client['ximalaya']
allAudio = ximalaya['allAudio']
test = ximalaya['test']


def getAudioUrl(id):
    idUrl = 'http://www.ximalaya.com/tracks/{}.json'.format(id)
    jsonContent = requests.get(idUrl, headers=headers).json()
    try:
        return jsonContent['play_path_64']  # 下载函数
    except:
        return


def getUrlHelp(itemInfo):
    _id = itemInfo['_id']
    soundId = itemInfo['soundId']
    audioUrl = getAudioUrl(soundId)
    # print(audioUrl)
    # allAudio.update_one({'_id': _id}, {'$set': {'audioUrl': audioUrl}})


if __name__ == '__main__':
    # pool = Pool()
    # pool = Pool(processes=40)
    # pool.map(getUrlHelp, allAudio.find().limit(10000))
    a = time.clock()
    threads = []
    for item in allAudio.find().limit(1000):
        # print(soundId)
        t1 = threading.Thread(target=getAudioUrl, args=(item['soundId'],))
        threads.append(t1)

    for t in threads:
        t.setDaemon(True)
        t.start()
        t.join()

    b = time.clock()
    print(b - a)
