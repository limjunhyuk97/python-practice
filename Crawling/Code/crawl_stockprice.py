import sys, selenium, usecsv, re, time

from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

def crawl_stock():
    driver = webdriver.Chrome(executable_path='chromedriver')
    driver.implicitly_wait(time_to_wait=6)

    URL = 'https://kr.investing.com/equities/south-korea'
    driver.get(url=URL)

    inner_content = driver.find_element_by_id("marketInnerContent")
    content_list = str(inner_content.text).split('\n')

    for i in range(len(content_list)):
        content_list[i].strip()
        content_list[i] = content_list[i].split()

    content_list[0][5] += " " + content_list[0][6]
    del content_list[0][6]

    for i in content_list:
        if content_list.index(i) == 0: continue
        cnt = 0
        for j in range(0, len(i)):
            if re.search('[a-zA-Z가-힣]', i[j]): cnt = j
            else: break
        for j in range(cnt):
            content_list[content_list.index(i)][0] += " " + content_list[content_list.index(i)][1]
            del content_list[content_list.index(i)][1]

    now = time.localtime()
    usecsv.writecsv(
        str(now.tm_year) + '_' + str(now.tm_mon) + ' ' + str(now.tm_mday) + '_' + str(now.tm_hour) + 'h' + str(
            now.tm_min) + 'm' + '_Stock.csv', content_list)
    driver.quit()

crawl_stock()

"""
# 원하는 주식 주가 정보 크롤링
while True:
    stock_name = input('추가할 주식 정보 (종료 시 N/n): ')
    if stock_name == "N" or stock_name == "n":
        now = time.localtime()
        usecsv.writecsv(
            str(now.tm_year) + '_' + str(now.tm_mon) + ' ' + str(now.tm_mday) + '__' + str(now.tm_hour) + ':' + str(
                now.tm_min) + ':' + str(now.tm_sec) + '_Stock.csv', content_list)
        driver.quit()

    search_box = driver.find_element_by_xpath("/html/body/div[5]/header/div[1]/div/div[3]/div[1]/input")
    search_box.send_keys(stock_name)
    search_box.send_keys(Keys.RETURN)

    destination = driver.find_element_by_xpath("/html/body/div[5]/section/div/div[2]/div[2]/div[1]/a").click()
    stock_info = []
    stock_info.append(stock_name)
    stock_info.append(driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div[1]/div[2]/div[1]/span").text)
    top_down = str(driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div[1]/div[2]/ul/li[3]/div[2]")).split()
    stock_info.append(top_down[0]); stock_info.append(top_down[1])
    stock_info.append(driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div[1]/div[2]/div[1]/div[2]/span[1]").text)
    stock_info.append(driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div[1]/div[2]/div[1]/div[2]/span[1]").text)
"""

