import time
import pymongo
client = pymongo.MongoClient('localhost', 27017)
wuba = client['wuba']
url_list = wuba['url_list']
item_info = wuba['item_info']
# while True:
#     print(url_list.find().count())
#     time.sleep(5)
a={'s':1,'d':2}
b=set([2,4,5,222,12])
print(a)