from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'https://www.baidu.com/s?wd=%E7%8A%AF%E7%BD%AA%E7%8E%B0%E5%9C%BA%E8%B0%83%E6%9F%A5'
driver = webdriver.Firefox()
driver.get(url)
# wb_data = driver.page_source
searchWord = '犯罪现场调查'
# search = driver.find_element_by_id('kw')
# search.send_keys(searchWord, Keys.ENTER)
# try:
#     WebDriverWait(driver, 0.5).until(EC.title_contains('胡歌'))
#     print('OVER33333333')
# finally:
#     print('OVER')


for i in range(3):
    page = 'https://www.baidu.com/s?wd={}&pn={}'.format(searchWord, str(i * 10))
    driver.get(page)
    items = driver.find_elements_by_xpath('//h3/a')
    root=driver.current_window_handle
    for i in range(len(items)):
        item=driver.find_elements_by_xpath('//h3/a')[i].click()

        driver.switch_to_window(root)
        time.sleep(0.5)
