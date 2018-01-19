from multiprocessing import Pool
from channel_extract import channel_list
from  page_parsing import get_links_form
from  page_parsing import get_item_info
from  page_parsing import url_list
from  page_parsing import item_info


def get_all_links_from(channel):
    for num in range(1, 101):
        get_links_form(channel, num)


def get_all_item(item_url):
    url = item_url['url']
    crb = item_url['crb']
    get_item_info(url, crb)


if __name__ == '__main__':
    # pool = Pool()
    pool = Pool(processes=40)
    pool.map(get_all_item, url_list.find())
# for url in item_info.find():
#     print(url)
