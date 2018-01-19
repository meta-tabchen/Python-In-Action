from multiprocessing import Pool
from channel_extract import channel_list
from  page_parsing import get_links_form
import pymongo

client = pymongo.MongoClient('localhost', 27017)
wuba = client['wuba']
url_list = wuba['url_list']
item_info = wuba['item_info']


def get_all_links_from(channel):
    for num in range(1, 101):
        get_links_form(channel, num)


if __name__ == '__main__':
    # pool = Pool()
    pool = Pool(processes=40)
    pool.map(get_all_links_from, channel_list.split())

# get_all_links_from('http://bj.58.com/tongxunyw/')
