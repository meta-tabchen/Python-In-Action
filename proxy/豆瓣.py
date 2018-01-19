from bs4 import BeautifulSoup
import requests
url='https://m.douban.com/doulist/240962/?start=50'
headers={
    'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.30'
}
wb_data=requests.get(url,headers=headers)

soup=BeautifulSoup(wb_data.text,'lxml')
titles=soup.select('h2')
ranks=soup.select('.rating-stars')
datas=[]
for title,rank in zip(titles,ranks):
    data={
        'title':title.get_text(),
        'rank':rank.get('data-rating')
    }
    datas.append(data)
datas=sorted(datas,key=lambda x : x['rank'],reverse=True)
for data in datas:
    print(data)