import pymongo
import os

client = pymongo.MongoClient('localhost', 27017)

ximalaya = client['ximalaya']
cataHelp = ximalaya['cateHelp']
allAudio = ximalaya['allAudio']
test = ximalaya['test']
allAlbum = ximalaya['allAlbum']





