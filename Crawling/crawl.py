import requests as req
import re

# HTTP GET : 요청, 값 가져옴
# HTTP POST : 생성
# HTTP PUT : 수정
# HTTP DELETE : 삭제


## [1] IP 주소 응답받기
'''
res = req.get("https://api.ipify.org/", headers={"lim" : "jun hyuk"})
print(res.request.method)       ## request 보낸 method
print(res.request.headers)      ## request로 보낸 header
print(res.status_code)          ## response로 받은 status code
print(res.text)                 ## response로 받은 html 그대로
print(res.raw)                  ## byte 값 그대로 받아서 사용하는 경우
print(res.elapsed)              ## request 보내고 받는데 걸린 시간
'''


## [2] XML / HTML / JSON
'''
1. XML : node 안에 정보를 감싸고 있는 문서.
2. HTML : XML에서 좀더 규칙이 생김. Tag(node)안에 정보를 감싸고 있는 문서. 
    - tag 단위로 붙어있는 id, class 같은 meta data를 attribute라고 한다.
    - div / span / p / li / button .. : text data를 담고 있는 주요 tag들
3. JSON : Java Script Object Notation
    - 매우 단순. JS의 기본 데이터 타입. Python의 dictionary와 유사한 타입
    - json beautifier를 사용하여 정돈하여 표현가능함
    - json 데이터 = "데이터 이름" : 값
    - json 객체 = { "데이터 이름1" : "값", "데이터 이름2" : "값", ...}
    - json 배열 = [ { 객체 1 }, { 객체 2 }, {객체 3}, ... ] 
'''


## [3] find / split
'''
### find : 특정 문자열의 존재 여부를 확인할 때에나 사용할 수 있다.
### split : split을 통해서 문자열을 찾는 것이 더 나을 수 있다.

s = '제 생일은 10월 입니다.'

pos = s.find('생일은 ') + 4
print(s[pos:pos+2])

### split앞부분[1].split뒷부분[0] : 원하는 문자열
print(s.split('생일은 ')[1].split('월')[0])

arr = [1, 2, 3, 4]
print(arr[:2])

res = req.get("https://finance.naver.com/marketindex/?tabSel=exchange#tab_section")
html = res.text

### split앞부분[1].split뒷부분[0] : 미국 환율 가져오기
print(html.split('<span class="value">')[1].split('</span>')[0])
'''


## [4] regular expression
'''
s = 'hilo'

print(re.match(r'hi', s))
print(re.match(r'.', s))
print(re.match(r'...', s))
print(re.match(r'hi1*', s))
print(re.match(r'hi1+', s))
print(re.match(r'hi1?', s))
print(re.match(r'ha?1*i+', s))

s2 = 'you goot?'
print(re.match(r'you good?', s2))
print(re.match(r'you good\?', s2))

s3 = 'H class'
print(re.match(r'[ABCDE] class', s3))
print(re.match(r'[ABCDEFGH.] class', s3))

s4 = '서울시 강남구 테헤란로'
print(re.findall(r'(..)시 (..)구 ([가-힇][가-힇][가-힇])로', s4))

### . : 아무 글자나 와도 됨 (\n을 포함하지 않는다.)
### .. : 아무 글자나 두글자 와도 됨
### 문자* : 어떤 문자가 0개 이상 오는 경우
### 문자+ : 어떤 문자가 1개 이상 오는 경우
### 문자? : 어떤 문자가 와도 되고 안되도 되는 경우
### \(* + ? .) : 특정 정규식단어를 무효화 할 수 있다.
### [문자들] : 어떤 문자들 중 아무거나
'''


## [5] 네이버 환율 crawl

### url 준비 -> get -> body 저장
url = "https://finance.naver.com/marketindex/?tabSel=exchange#tab_section"
res = req.get(url)
body = res.text

### 정규표현식 준비 (re.DOTALL : *에 \n도 포함한다, ? : 가장 가까운 부분까지만으로 제한한다.)
r = re.compile(r'"h_lst".*?"blind">(.*?)</span>.*?value">(.*?)</', re.DOTALL)
captures = r.findall(body)

print("----- 환율 계산기 -----")
for i in captures:
    print(i[0] + " : " + i[1])
print("--------------------")
usd = float(captures[0][1].replace(",", ""))
won = input("달러로 바꾸려하는 원을 입력하세요 : ")
won = int(won)
print(int(won/usd))














