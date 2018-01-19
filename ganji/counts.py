import time
import pymongo
client = pymongo.MongoClient('localhost', 27017)
ganji = client['ganji']
url_list = ganji['item_infoss']
while True:
    print(url_list.find().count())
    time.sleep(2)