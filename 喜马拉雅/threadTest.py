from bs4 import BeautifulSoup
import pymongo
import threading
from lxml import etree
from multiprocessing import Pool
import requests
import os
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 '
}

client = pymongo.MongoClient('localhost', 27017)
ximalaya = client['ximalaya']
allAudio = ximalaya['allAudio']
allAlbum = ximalaya['allAlbum']
titleHelp = ximalaya['titleHelp']

def getAudioUrl(id):
    idUrl = 'http://www.ximalaya.com/tracks/{}.json'.format(id)
    jsonContent = requests.get(idUrl, headers=headers).json()
    try:
        return jsonContent['play_path_64']  # 下载函数
    except:
        pass

# 获取一个专辑里的所有音频链接
def getOneAlbum(albumUrl, albumTitle, title, cate, albumId):
    wb_data = requests.get(albumUrl, headers=headers)
    selector = etree.HTML(wb_data.content)

    names = selector.xpath('//*[@class="title"]/@title')
    soundIds = selector.xpath('//*[@id="mainbox"]/div/div[1]/div/div[2]/div[4]/ul/li/@sound_id')

    for soundId, name in zip(soundIds, names):
        try:
            data = {
                'name': name,
                'soundId': soundId,
                'audioUrl': getAudioUrl(soundId),
                'albumTitle': albumTitle,
                'cate': cate,
                'title': title,
                'albumUrl': albumUrl,
                'albumId': albumId
            }
            allAudio.insert_one(data)
        except:
            pass


def getOneAlbumHelp(albumInfo):
    albumId = albumInfo['_id']
    albumUrl = albumInfo['albumUrl']
    albumTitle = albumInfo['albumTitle']
    title = albumInfo['title']
    cate = albumInfo['cate']
    getOneAlbum(albumUrl, albumTitle, title, cate, albumId)

def threadHelp(title):
    title = ximalaya[title]
    threads = []
    for album in title.find():
        t1 = threading.Thread(target=getOneAlbumHelp, args=(album,))
        threads.append(t1)
    for t in threads:
        t.setDaemon(True)
        t.start()
        t.join()

if __name__ == '__main__':
    pool = Pool()
    pool = Pool(processes=20)
    titles = set([x['title'] for x in allAlbum.find()])
    titleHelp=[]
    # 对每一个分类开始查找
    for i in range(len(titles)):
        titleHelp.append(titles.pop())
    pool.map(threadHelp, titleHelp)
#     # print(titleHelp)
