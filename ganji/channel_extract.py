from bs4 import BeautifulSoup
import requests
start_url='http://cc.ganji.com/wu/'
url_host='http://cc.ganji.com'
def get_channel_urls(url):
    wb_data=requests.get(start_url)
    soup=BeautifulSoup(wb_data.text,'lxml')
    links =soup.select('div.content dt a')
    for link in links:
        page_url=url_host+link.get('href')
        print(page_url)
# get_channel_urls(start_url)
#长串的字符用''' '''
channel_list = '''
http://cc.ganji.com/jiaju/
http://cc.ganji.com/rirongbaihuo/
http://cc.ganji.com/shouji/
http://cc.ganji.com/jiadian/
http://cc.ganji.com/ershoubijibendiannao/
http://cc.ganji.com/ruanjiantushu/
http://cc.ganji.com/yingyouyunfu/
http://cc.ganji.com/diannao/
http://cc.ganji.com/fushixiaobaxuemao/
http://cc.ganji.com/meironghuazhuang/
http://cc.ganji.com/shuma/
http://cc.ganji.com/laonianyongpin/
'''