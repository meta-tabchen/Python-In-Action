import pymongo

client = pymongo.MongoClient('localhost', 27017)
ganji = client['ganji']
url_list = ganji['url_list']
item_infoss = ganji['item_infoss']
item_infos = ganji['item_infos']
# print(url_list.find().count())
# print(item_infos.find({'url':'http://zhuanzhuan.ganji.com/detail/860047914058235915z.shtml'}).count())
db_urls = [item['url'] for item in item_infos.find()]  # 用列表解析式装入所有要爬取的链接
urls=set(db_urls)
for url in urls:
    item_infoss.insert_one({'url': url})
