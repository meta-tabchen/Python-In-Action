from bs4 import BeautifulSoup
import requests
import time
import pymongo
import re
from channel_extract import channel_list

client = pymongo.MongoClient('localhost', 27017)
ganji = client['ganji']
url_list = ganji['url_list']
item_info = ganji['item_info']


# 用来抓取每个分类页面下item的url

def get_links_form(channel, pages, who_sells=1):
    time.sleep(1)
    page_url = '{}o{}/'.format(channel, str(pages))
    wb_data = requests.get(page_url)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    if soup.find('div', 'noinfo'):
        # print('没有内容')
        pass
    else:
        #分类合集
        crb=soup.select('.nav span')[0].text
        links = soup.select('tr[class="zzinfo "]  td.t  a')  # 通过这种形式筛选
        for item_link in links:
            item_link = item_link.get('href').split('?')[0]
            url_list.insert_one({'url': item_link, 'crb': crb})
        # print(links)
        # for item_link in links:
        #     i=0
        #     item_link = item_link.get('href').split('?')[0]
        #     for temp_url in url_list.find():
        #         if(temp_url['url']==item_link):
        #             i=i+1
        #     if (i==0):
        #         url_list.insert_one({'url': item_link,'crb':crb})
                # get_item_info(item_link,crb)
                # print('insert------------------------')
                # print(item_link)

# 获取每个item的详细信息
def get_item_info(url,crb):

    # i = 0
    # for temp_url in item_info.find():
    #     if (temp_url['url'] == url):
    #         i = i + 1
    # if (i == 0):
    try:
        wb_data = requests.get(url)
        soup = BeautifulSoup(wb_data.text, 'lxml')
        title = soup.select('.info_titile')[0].text
        description = soup.select('.baby_kuang p')[0].text if soup.find('.baby_kuang p') else '无地址'
        oldPrice = soup.select('.price_now b')[0].text if soup.find('b', 'price_ori') else '0'
        newPrice = soup.select('.price_now i')[0].text
        if '万' in newPrice:
            newPrice = re.sub("\D", "", newPrice) + '0000'
        if '万' in oldPrice:
            oldPrice = re.sub("\D", "", oldPrice) + '0000'
        # print(url)
        address = list(soup.select('.palce_li')[0].stripped_strings)[1]
        biaoqian = list(soup.select('.biaoqian_li')[0].stripped_strings)
        look_time = re.sub("\D", "", soup.select('.look_time')[0].text)
        want_person = re.sub("\D", "", soup.select('.want_person')[0].text)
        name = soup.select('p.personal_name')[0].text
        achievement = re.sub("\D", "", soup.select('p.personal_chengjiu')[0].text)

        item_info.insert_one(
            {'title': title, 'description': description, 'oldPrice': oldPrice, 'newPrice': newPrice, 'address': address,
             'biaoqian': biaoqian,
             'look_time': look_time, 'want_person': want_person, 'url': url, 'crb': crb})


        # data={'title': title, 'description': description, 'oldPrice': oldPrice, 'newPrice': newPrice, 'address': address,'biaoqian':biaoqian,
        #      'look_time': look_time,'want_person':want_person,'name':name,'achievement':achievement,'url':url}
    except:
        pass


def get_all_link(url,start,end):
    for i in range(start,end):
        # time.sleep(1)
        get_links_form(url,i)
# get_all_link('http://cc.ganji.com/shuma/',1,3)

# for cateUrl in channel_list.split():
#     get_all_link(cateUrl, 1, 2)
# get_item_info('http://zhuanzhuan.ganji.com/detail/742268208400547841z.shtml')
# get_links_form('http://cc.ganji.com/jiaju/',4)
get_item_info('http://zhuanzhuan.ganji.com/detail/860047914058235915z.shtml','ff')