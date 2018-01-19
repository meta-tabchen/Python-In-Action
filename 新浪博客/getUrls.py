import requests
from bs4 import BeautifulSoup
url='http://blog.sina.com.cn/s/articlelist_5710278057_0_1.html'
wb_data=requests.get(url)
soup=BeautifulSoup(wb_data.text,'lxml')
links=soup.select('#module_928 > div.SG_connBody > div.article_blk > div.articleList > div > p.atc_main.SG_dot > span.atc_title > a')
for link in links:
    print(link.get('href'))