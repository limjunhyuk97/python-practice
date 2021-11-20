'''
201820740 임준혁
Ajou BB, class notice 최신화하여 끌고오기
'''


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
import os, re, time, usecsv

from bs4 import BeautifulSoup as bs

## driver를 chrome으로 설정
browser = webdriver.Chrome()

## browser에서 특정 URL에 접근 / 페이지가 로드될 때까지 암시적 대기 / 로그인
browser.get("https://eclass2.ajou.ac.kr/ultra/course")
browser.implicitly_wait(2)

browser.find_element_by_id('userId').send_keys('...')
browser.find_element_by_id('password').send_keys('...')
browser.find_element_by_id('loginSubmit').click()

## 2021학년 2학기 과목들에 부여된 고유번호 확인
main_page = browser.current_url
course_list = []
course_list.append('https://eclass2.ajou.ac.kr/ultra/courses/_69810_1/cl/outline')
course_list.append('https://eclass2.ajou.ac.kr/ultra/courses/_67670_1/cl/outline')
course_list.append('https://eclass2.ajou.ac.kr/ultra/courses/_69880_1/cl/outline')
course_list.append('https://eclass2.ajou.ac.kr/ultra/courses/_70347_1/cl/outline')
course_list.append('https://eclass2.ajou.ac.kr/ultra/courses/_69504_1/cl/outline')
course_list.append('https://eclass2.ajou.ac.kr/ultra/courses/_69501_1/cl/outline')

announcement_list = {}
for i in course_list:
    browser.get(i); browser.implicitly_wait(10)
    next = browser.find_element_by_css_selector('button-6').get_attribute('href')
    browser.get(next)
    ## 공지사항으로 이동 후에 페이지 소스 추출, soup 객체에 저장
    html = browser.page_source
    soup = bs(html, 'html.parser')
    ## soup로 공지사항 추출
    target_ul = soup.find_all("ul", {'id' : 'announcementList'})
    for lii in target_ul:
        title = lii.find('li', {'class' : 'clearfix'})
        details = lii.find('div', {'class' : 'details'})
        main = lii.find('div', {'class' : 'vtbegenerated'})
        info = lii.find('div', {'class' : 'announcementInfo'})
        print('title : ' + title.text)
        print('details : ' + details.text)
        print('main : ' + main.text)
        print('info : ' + info.text)
    browser.get(main_page)

# browser 종료
exit_browser = input('exit? : ')
if exit_browser == 'yes':
    browser.close()

