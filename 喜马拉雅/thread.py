import threading
import requests
import time
from lxml import etree
from time import ctime, sleep

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

def getAudioUrl(id):
    idUrl = 'http://www.ximalaya.com/tracks/{}.json'.format(id)
    jsonContent = requests.get(idUrl, headers=headers).json()
    # try:
    # print(jsonContent)
    # return jsonContent['play_path_64']  # 下载函数
    # except:
    #     pass  # 获取一个专辑里的所有音频链接
def getOneAlbum(albumUrl):
    wb_data = requests.get(albumUrl, headers=headers)
    selector = etree.HTML(wb_data.content)

    names = selector.xpath('//*[@class="title"]/@title')
    soundIds = selector.xpath('//*[@id="mainbox"]/div/div[1]/div/div[2]/div[4]/ul/li/@sound_id')
    audioUrls = getAll(soundIds)
    # for soundId, name in zip(soundIds, names):
    #     try:
    #         data = {
    #             'name': name,
    #             'soundId': soundId,
    #             'audioUrl': audioUrls[soundId],
    #             'albumUrl': albumUrl,
    #         }
    # except:
    #     pass


def getAll(soundIds):
    audioUrls = []
    threads = []
    for soundId in soundIds:
        # print(soundId)
        t1 = threading.Thread(target=getAudioUrl, args=(soundId,))
        threads.append(t1)

    for t in threads:
        t.setDaemon(True)
        t.start()
        t.join()
        # print("all over %s" % ctime())


a = time.clock()
getOneAlbum('http://www.ximalaya.com/1000519/album/3519155')
b = time.clock()
print(b - a)
