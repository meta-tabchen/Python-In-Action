import requests

commentUrl = 'http://m.weibo.cn/api/comments/show?id={}&page=1'
f = open("张子见.txt", 'w', encoding='utf-8')


def getComment(id):
    url = commentUrl.format(str(id))
    try:
        datas = requests.get(url, verify=False).json()['hot_data']
    except:
        return
    for data in datas:
        if (data['user']['screen_name'] == '爱秋天的菇凉子'):
            f.write('\n')
            f.write('解析：')
            f.write('\n')
            f.write(data['text'].strip())
            f.write('\n')
            f.write('\n')
            break


def getNews(cards):
    for card in cards:
        mblog = card['mblog']
        id = mblog['id']
        extendUrl = 'https://m.weibo.cn/statuses/extend?id={}'.format(id)
        data = requests.get(extendUrl, verify=False).json()
        text = data['longTextContent']
        text = text.split("<br/>")

        for i in text:
            f.write(i)
            f.write('\n')
            # print(i)
        getComment(id)


def getPages(a, b):
    for page in range(a, b + 1):
        mainPageUrl = 'https://m.weibo.cn/api/container/getIndex?uid=5350904556&luicode=10000011&lfid=1076035350904556&type=uid&value=5350904556&containerid=1076035350904556&page={}'.format(
            page)
        date = requests.get(mainPageUrl, verify=False).json()
        cards = date['cards']
        # print(cards)
        getNews(cards)
        f.flush()

getPages(1, 1)
