from bs4 import BeautifulSoup
import requests
import time
import pymongo
from channel_extract import channel_list

client = pymongo.MongoClient('localhost', 27017)
wuba = client['wuba']
url_list = wuba['url_list']
item_info = wuba['item_info']


# spider 1

def get_links_form(channel, pages=2, who_sells=1):
    try:
        # http://bj.58.com/bijiben/0/pn10
        list_view = '{}{}/pn{}'.format(channel, str(who_sells), str(pages))
        wb_data = requests.get(list_view)
        time.sleep(1)
        soup = BeautifulSoup(wb_data.text, 'lxml')
        if soup.find('td', 't'):
            links = soup.select('td.t > a.t ')
            for link in links:
                item_link = link.get('href')
                url_list.insert_one({'url': item_link})
                # get_item_info(item_link)
                # print(item_link)
            else:
                pass
    except:
        pass


def get_item_info(url):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    no_longer_exist = '404' in soup.find('script', type="text/javascript").get('src').split('/')
    if no_longer_exist:
        pass
    else:
        soup = BeautifulSoup(wb_data.text, 'lxml')
        sorts = soup.select('span.crb_i')[0].text if soup.find_all('span', 'crb_i') else None
        price = list(soup.select('.c_f50')[0].stripped_strings)[0] if soup.find_all('span',
                                                                                    'c_f50') else None
        title = soup.select('.mainTitle h1')[0].text
        time = soup.select('li.time')[0].text if soup.find_all('li', 'time') else None
        area = list(soup.select('.c_25d')[0].stripped_strings) if soup.find_all('span', 'c_25d') else None
        # item_info.insert_one({'title': title,'sorts':sorts, 'price': price, 'time': time, 'area': area, 'url': url})
        print({'title': title, 'sorts': sorts, 'price': price, 'time': time, 'area': area, 'url': url})


get_item_info('http://bj.58.com/shouji/29945504311599x.shtml')
