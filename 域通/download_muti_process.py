import requests
import re
from multiprocessing import Pool


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

    # def go():


if __name__ == '__main__':
    print('start')
    pool = Pool()
    pool = Pool(processes=50)
    pool.map(test, range(50))
