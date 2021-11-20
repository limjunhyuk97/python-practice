from selenium import webdriver
import time

def crawl_naver(id, pwd):
    # driver를 chrome으로 설정
    browser = webdriver.Chrome()

    # browser에서 특정 URL에 접근 / 페이지가 로드될 때까지 암시적 대기
    browser.get('https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com')
    browser.implicitly_wait(2)

    browser.find_element_by_id('id').send_keys(id)
    browser.find_element_by_id('pw').send_keys(pwd)
    browser.find_element_by_id('log.login').click()

    # 페이지의 소스를 html이라는 변수가 가리키게 함
    html = browser.page_source
    with open('naver_login', 'w') as f:
        f.write(html)

    # 작업이 끝나면 browser 종료
    browser.close()

    return html
