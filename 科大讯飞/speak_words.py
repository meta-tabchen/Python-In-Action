import requests
import time
import urllib.parse

vid = "68010"


def get_sign(content):
    url = 'http://www.peiyinge.com/make/getSynthSign'
    data = 'content={}'.format(content).encode('utf-8')
    headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
    result = requests.post(url, headers=headers, data=data).json()
    return result['sign'], result['ts']


def download_sample(content):
    sign, ts = get_sign(content)
    url = 'http://proxy.peiyinge.com:17063/synth?ts={}&sign={}&vid={}&volume=0&speed=0&content={}'.format(ts, sign, vid,
                                                                                                          content)
    f = open('sample.mp3', 'wb')
    result = requests.get(url)
    f.write(result.content)
    # print(int(time.time()))


def set_user():
    import json
    data = open('主播声音.json', 'r', encoding='utf-8')
    data = json.load(data)
    count = 0
    for i in data:
        print(count, i)
        count = count + 1
    choose_index = int(input("输入序号\n"))
    # group = "方言主播"
    choose_index = list(data.keys())[choose_index]
    print(choose_index)
    data = data[choose_index]['body']['speakers']
    count = 0
    for i in data:
        print(count, i['speaker_style'])
        count = count + 1
    choose_index = int(input("输入序号\n"))
    global vid
    vid = data[choose_index]['speaker_no']
    print(vid)


str = '''酒要一口一口喝，路要一步一步走，步子迈得太大，容易扯着蛋。'''

set_user()
print(vid)
download_sample(str)
