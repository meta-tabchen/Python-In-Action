from selenium import webdriver
from bs4 import BeautifulSoup

import requests

url = 'https://s.taobao.com/search?q=%E5%B9%B3%E6%9D%BF%E7%94%B5%E8%84%91&p4ppushleft=5%2C48&s=48'
driver = webdriver.PhantomJS()
driver.get(url)
# f = open('淘宝data', 'r',encoding='utf-8')
# wb_data=f.read()
wb_data=driver.page_source
soup=BeautifulSoup(wb_data,'lxml')
imgs=soup.select('.J_ItemPic')
prices=soup.select('.g_price strong')
titles=soup.select('.product-title')
weekSales=soup.select('.week-sale span')
print(len(imgs))
print(len(prices))
print(len(titles))
print(len(weekSales))
for img,price,title,weekSale in zip(imgs,prices,titles,weekSales):
    data={
        'img':'https:'+img.get('src'),
        'price':price.get_text(),
        'title':title.get('title'),
        'weekSale':weekSale.get_text()
    }
    print(data)
