from bs4 import BeautifulSoup
from lxml import etree
from multiprocessing import Pool
import requests
import os
import time
import threading

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 '
}


def getAudioUrl(id):
    idUrl = 'http://www.ximalaya.com/tracks/{}.json'.format(id)
    jsonContent = requests.get(idUrl, headers=headers).json()
    try:
        return jsonContent['play_path_64']  # 下载函数
    except:
        pass


def downloadAudio(dir, title, soundId):
    print(title)
    audioUrl = getAudioUrl(soundId)
    # print(title)
    try:
        wb_data = requests.get(audioUrl)
        name = '{}/{}.m4a.'.format(dir, title)
        with open(name, 'wb') as f:
            f.write(wb_data.content)
    except:
        print('付费节目')


# 获取一个专辑里的所有音频链接
def getOneAlbum(albumUrl):
    if 'http://' not in albumUrl:
        getAlubmUrl(albumUrl)
    else:
        wb_data = requests.get(albumUrl, headers=headers)
        selector = etree.HTML(wb_data.content)
        try:
            title = selector.xpath('//*[@class="detailContent_title"]/h1/text()')[0]
        except:
            return
        if not os.path.exists(title):
            os.mkdir(title)

        for page in range(1, 8):
            url = '{}?page={}'.format(albumUrl, str(page))
            wb_data = requests.get(url, headers=headers)

            # 如果没有页面没有了音频则停止
            if 'album_soundlist' not in wb_data.text:
                break
            wb_data = requests.get(url, headers=headers)
            selector = etree.HTML(wb_data.content)

            names = selector.xpath('//*[@class="title"]/@title')
            soundIds = selector.xpath('//*[@id="mainbox"]/div/div[1]/div/div[2]/div[4]/ul/li/@sound_id')

            threads = []

            for soundId, name in zip(soundIds, names):
                t1 = threading.Thread(target=downloadAudio, args=(title, name, soundId,))
                threads.append(t1)

            for t in threads:
                t.setDaemon(True)
                t.start()
                t.join()


def getAlubmUrl(name):
    url = 'http://www.ximalaya.com/search/{}/t3s3'.format(name)
    try:
        wb_data = requests.get(url, headers=headers)
        selector = etree.HTML(wb_data.content)

        albumUrls = selector.xpath('//*[@class="content_wrap2"]/div[1]/a/@href')
        if(len(albumUrls)==0):
            print("没有找到请重新输入")
            getStart()

        for albumUrl in albumUrls:
            host = 'http://www.ximalaya.com'
            albumUrl = host + albumUrl
            print(albumUrl)
            getOneAlbum(albumUrl)
    except:
        print('呀你真厉害，难到我了')
def  getStart():
    keyWord=input("输入专辑名或者链接：\n")
    getOneAlbum(keyWord)
getStart()