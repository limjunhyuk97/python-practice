from selenium import webdriver
import time

def crawl_page(URL, file_name):
    # driver를 chrome으로 설정
    browser = webdriver.Chrome()

    # browser에서 특정 URL에 접근 / 페이지가 로드될 때까지 암시적 대기
    browser.get(URL)
    browser.implicitly_wait(2)

    # 페이지의 소스를 html이라는 변수가 가리키게 함
    html = browser.page_source
    with open(file_name, 'w') as f:
        f.write(html)

    # 작업이 끝나면 browser 종료
    browser.close()

    return html
