# coding=utf-8
import threading
import requests
import re


def download(url, filename="temp.pdf"):
    print(filename, 'is start')
    wb_data = requests.get(url)
    f = open(filename, "wb")
    f.write(wb_data.content)
    print(filename, "download over")


def get_detail_url(url=""):
    wb_data = requests.get(url, verify=False)
    url = re.findall("free_down_action\('(.+?)'", wb_data.text)[0]
    return url


furls = open('urls.txt', 'r').read().strip().split('\n')
fnames = open('names.txt', 'r').read().strip().split('\n')


def test(i):
    download(furls[i], fnames[i])


threads = []
for i in range(len(furls)):
    t1 = threading.Thread(target=test, args=(i,))
    threads.append(t1)


def start():
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print("all is over")


start()
