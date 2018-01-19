from bs4 import BeautifulSoup
from lxml import etree
import pymongo
from multiprocessing import Pool
import requests
import os
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 '
}

client = pymongo.MongoClient('localhost', 27017)
ximalaya = client['ximalaya']
allPage = ximalaya['allPage']
allAlbum = ximalaya['allAlbum']
allAudio = ximalaya['allAudio']


def getAudioUrl(id):
    idUrl = 'http://www.ximalaya.com/tracks/{}.json'.format(id)
    jsonContent = requests.get(idUrl, headers=headers).json()
    try:
        return jsonContent['play_path_64']  # 下载函数
    except:
        pass

# 获取一个专辑里的所有音频链接
def getOneAlbum(albumUrl, albumTitle, title, cate, albumId):
    # print(albumUrl, albumTitle)

    wb_data = requests.get(albumUrl, headers=headers)
    selector = etree.HTML(wb_data.content)

    names = selector.xpath('//*[@class="title"]/@title')
    soundIds = selector.xpath('//*[@class="album_soundlist "]/ul/li/@sound_id')

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
    # if albumId in checks:
    #     print(albumId)
    #     return
    albumUrl = albumInfo['albumUrl']
    albumTitle = albumInfo['albumTitle']
    title = albumInfo['title']
    cate = albumInfo['cate']
    getOneAlbum(albumUrl, albumTitle, title, cate, albumId)



# albumInfos = [x for x in allAlbum.find()]
# checks = [x['albumId'] for x in allAudio.find()]
# print('albumInfos Over')
#

if __name__ == '__main__':
    pool = Pool()
    pool = Pool(processes=80)
    pool.map(getOneAlbumHelp, allAlbum.find())
