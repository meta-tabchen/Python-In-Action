#######
# 资源链接http://jiaofu.yousi.com
#
#
#######


from bs4 import BeautifulSoup
import requests
import re

host = 'http://jiaofu.yousi.com'

info = {'高中': '35', '初中': '34', '小学': '33', '数学': '10', '语文': '12', '英语': '11', '化学': '8', '物理': '9', '生物': '13',
        '政治': '14', '历史': '15', '地理': '16', '科学': '17', '奥数': '18'}


# 下载书籍
def download(name, url):
    data = requests.get(url)
    f = open(name.strip() + '.pdf', 'wb')
    f.write(data.content)
    f.flush()
    f.close()


# 获取书籍的链接
def pdf_url(url):
    url = host + url
    wb_data = requests.get(url).text
    pattern = '[\d]{18}.pdf'
    result = re.findall(pattern, wb_data)[0]
    return 'http://jfpdf.yousi.com/{}'.format(result)


# 获取一个分类下所有的书籍
def one_page(url=''):
    # url = 'http://jiaofu.yousi.com/l-35-9-0-2/'
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    lession_infos = soup.select('body > div.jf-teach > div.jf-box > ul > li > p > a')
    print(soup.select('title'))
    for lession_info in lession_infos:
        lession_name = lession_info.getText()
        lession_url = lession_info.get('href')
        print('正在下载', '>' * 10, lession_name)
        download(lession_name, pdf_url(lession_url))


# 获取科目列表，一般不用
def lesson_list(url='http://jiaofu.yousi.com/l-33-12-0-0/'):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    print(soup.select('title'))
    list = soup.select('body > div.jf-teach > div.lesson-list > div > ul.fn-right.right > li > a')
    print(list)
    a = {}
    for i in list:
        a[i.getText()] = i.get('href').split('-')[3]
    print(a)


# 获取教材版本
def get_version(url='http://jiaofu.yousi.com/l-35-9-0-0/'):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    result = soup.select('body > div.jf-teach > div.lesson-list > div:nth-of-type(3) > ul.fn-right.right > li > a')
    versions = {}
    for i in result:
        versions[i.getText()[:1]] = host + i.get('href')
    return versions


# 下载一个科目的教材
def download_subject(grade='高中', subject='物理'):
    # grade = '高中'
    # subject = '物理'
    url = 'http://jiaofu.yousi.com/l-{}-{}-0-0/'.format(info[grade], info[subject])
    versions = get_version(url)
    title = list(versions.keys())
    print(title)
    select = input('\n输入版本:').strip()
    print('开始下载')
    one_page(versions[select])


download_subject('高中','数学')
