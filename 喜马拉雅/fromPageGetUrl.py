from bs4 import BeautifulSoup
import pymongo
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
allPage = ximalaya['allPage']
allAlbum = ximalaya['allAlbum']
allAlbum2 = ximalaya['allAlbum2']
allAudio = ximalaya['allAudio']


def getAudioUrl(id):
    idUrl = 'http://www.ximalaya.com/tracks/{}.json'.format(id)
    jsonContent = requests.get(idUrl, headers=headers).json()
    try:
        return jsonContent['play_path_64']  # 下载函数
    except:
        pass


def downloadAudio(dir, title, audioUrl):
    time.sleep(2)
    wb_data = requests.get(audioUrl)
    name = '{}/{}.m4a.'.format(dir, title)
    with open(name, 'wb') as f:
        f.write(wb_data.content)


# 获取一个专辑里的所有音频链接
def getOneAlbum(albumUrl, albumTitle, title, cate, albumId):
    wb_data = requests.get(albumUrl, headers=headers)
    selector = etree.HTML(wb_data.content)

    for page in range(1, 10):
        url = '{}?page={}'.format(albumUrl, str(page))
        wb_data = requests.get(url, headers=headers)

        # 如果没有页面没有了音频则停止
        if 'album_soundlist' not in wb_data.text:
            break
        wb_data = requests.get(url, headers=headers)
        selector = etree.HTML(wb_data.content)
        names = selector.xpath('//*[@class="title"]/@title')
        soundIds = selector.xpath('//*[@id="mainbox"]/div/div[1]/div/div[2]/div[4]/ul/li/@sound_id')

        for soundId, name in zip(soundIds, names):
            try:
                data = {
                    'name': name,
                    '_id': soundId,
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
    allAlbum2.remove({'_id':albumInfo['_id']})
    # print(albumInfo)


# 获取页面里所有的专辑链接
def getAlbums(pageUrl, cate, title):
    print(pageUrl, cate, title)
    wb_data = requests.get(pageUrl, headers=headers)
    soup = BeautifulSoup(wb_data.text, 'lxml')

    albumUrls = soup.select('.albumfaceOutter > a')
    # 自动检测是否为空的情况
    if (len(albumUrls) != 0):
        albumTitles = soup.select('a.discoverAlbum_title')
        for albumUrl, albumTitle in zip(albumUrls, albumTitles):
            data = {
                'albumUrl': albumUrl.get('href'),
                'albumTitle': albumTitle.get('title'),
                'title': title,
                'cate': cate
            }
            allAlbum.insert(data)
    else:
        pass


def getAlbumsHelp(pageInfo):
    for i in range(85):
        pageUrl = pageInfo['pageUrl']
        cate = pageInfo['cate']
        title = pageInfo['title']
        pageUrl = '{}{}'.format(pageUrl, str(i))
        try:
            getAlbums(pageUrl, cate, title)
        except:
            pass


# 获取所有分类的页面
def getPages(url):
    host = 'http://www.ximalaya.com'
    wb_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    pageUrls = soup.select('.tagBtn')
    for pageUrl in pageUrls:
        pageUrl = pageUrl.get('href')
        cate = pageUrl.split('-')[0].split('/')[2]
        title = pageUrl.split('-')[1].strip('/')
        pageUrl = host + pageUrl;
        data = {
            'cate': cate,
            'title': title,
            'pageUrl': pageUrl
        }
        allPage.insert_one(data)
        # print(data)


# pageUrls = [x for x in allPage.find()]

# getPages('http://www.ximalaya.com/dq/all/')
# albumInfos = [x for x in allAlbum.find()]
# print('albumInfos Over')
#

if __name__ == '__main__':
    pool = Pool()
    pool = Pool(processes=80)
    pool.map(getOneAlbumHelp, allAlbum2.find())
