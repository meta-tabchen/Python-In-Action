import pymongo
import time
from string import punctuation
client = pymongo.MongoClient('localhost', 27017)
ximalaya = client['ximalaya']
alubms = ximalaya['allAudio']
while True:

    a = alubms.find().count()
    time.sleep(2)
    b = alubms.find().count()
    print('总数' + str(b))
    # print('分钟速',(alubms.find().count() - a)*2)
    print('时速',(b - a) *3* 60)