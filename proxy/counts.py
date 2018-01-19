import pymongo
import time
from string import punctuation

client = pymongo.MongoClient('localhost', 27017)
proxy = client['proxy']
good = proxy['good']
help = proxy['help']
raw=proxy['raw']
while True:
    a = good.find().count()
    time.sleep(10)
    print("good总数" + str(good.find().count()))
    print("核查总数" + str(help.find().count()))
    # print(raw.find().count())
    # time.sleep(10)