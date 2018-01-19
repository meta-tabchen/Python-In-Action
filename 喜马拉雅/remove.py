import pymongo

client = pymongo.MongoClient('localhost', 27017)

ximalaya = client['ximalaya']
cataHelp = ximalaya['cateHelp']
allAudio = ximalaya['allAudio']
test = ximalaya['test']
allAlbum = ximalaya['allAlbum']
allAlbum2 = ximalaya['allAlbum2']

def removeAlbum():
    x = set([x['title'] + '|' + x['albumUrl'] + '|' + x['cate'] + '|' + x['albumTitle'] for x in allAlbum.find()])
    print(len(x))
    # allAlbum.remove()
    # for i in range(len(x)):
    #     item = x.pop()
    #     item = item.split('|')
    #     allAlbum2.insert_one({'title': item[0], 'albumUrl': item[1], 'cate': item[2], 'albumTitle': item[3]})
    # allAlbum.remove()
    # for item in allAlbum2.find():
    #     allAlbum.insert_one(item)
def removeAudio():
    x = set([x['title'] + '|' + x['albumUrl'] + '|' + x['cate'] + '|' + x['albumTitle'] +'|'+x['name']+x['audioUrl'] for x in allAudio.find()])
    print(len(x))
# removeAudio()
print(allAudio.find().count())