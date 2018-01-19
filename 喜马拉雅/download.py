from bs4 import BeautifulSoup
import pymongo
from lxml import etree
from multiprocessing import Pool
import requests
import os
import time


client = pymongo.MongoClient('localhost', 27017)
ximalaya = client['ximalaya']
allAlbum = ximalaya['allAlbum']
allAudio = ximalaya['allAudio']
f=open('url.txt','w')
# os.mkdir('大宋的智慧')


def downloadAudio(fileInfo):
    audioUrl = fileInfo['audioUrl']
    albumTitle = fileInfo['albumTitle']
    name = fileInfo['name']

    wb_data = requests.get(audioUrl)
    name = '{}/{}.m4a.'.format(albumTitle, name)
    with open(name, 'wb') as f:
        f.write(wb_data.content)

for i in allAudio.find({'albumTitle':'大宋的智慧'}):
    # print(i)
   downloadAudio(i)

