import pymongo

client = pymongo.MongoClient('localhost', 27017)

ximalaya = client['ximalaya']
allAlbum = ximalaya['allAlbum']
cates = set([x['cate'] for x in allAlbum.find()])
# print(cates)
allCate=[]
for i in range(len(cates)):
    cate = cates.pop()
    titleDb = ximalaya[cate]
    allCate.append({'cate':cate,'count':titleDb.find().count()})
    # for item in allAlbum.find({'cate': cate}):
    #     titleDb.insert(item)
allCate=sorted(allCate,key=lambda  x : x['count'])
print(allCate)