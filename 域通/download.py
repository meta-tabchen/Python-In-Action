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


def download_all(urls_file_path='urls.txt', filenames_file_path='names.txt'):
    urls = open(urls_file_path, 'r').read().strip().split('\n')
    filenames = open(filenames_file_path, 'r').read().strip().split('\n')
    threads = []
    def test(i):
        download(urls[i], filenames[i])

    for i in range(len(urls)):
        t1 = threading.Thread(target=test, args=(i,))
        threads.append(t1)
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print("all is over")


def get_url_and_name_one_file(filepath='urls.txt'):
    all_item = open(filepath, 'r').read().strip().split('\n')
    all_name = []
    all_url = []
    for item in all_item:
        print(item)
        item = item.split(':::')
        print(item)
        all_name.append(item[0])
        all_url.append(item[1])
    return all_url, all_name
