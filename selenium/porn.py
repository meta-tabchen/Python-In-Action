from selenium import webdriver
from lxml import etree
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

url = 'https://www.youjizz.com/videos/no-pants-dance-38779251.html'
driver = webdriver.Chrome()
driver.get(url)

driver.get(
    'https://www.youjizz.com/videos/backseat-hot-fuck-20937161.html')  # wb_data = requests.get(video, headers=headers).content
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, 'source'))
    )
finally:
    wb_data = driver.page_source
    selector = etree.HTML(wb_data)
    host = 'http://hhh600.com'
    pages = selector.xpath('//source/@src')
    src = pages[0]
    src = 'https:' + src
print(src)
