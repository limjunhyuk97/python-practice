# CSV 가공
  - Notepad++
  - excel
  - python

## 01. CSV 파일
  - 쉼표로 나눠진 값들을 저장한 데이터
  - 서식정보를 배제한 원형 그대로의 가공하기 좋은 데이터 형식이다.
  - **웹문서 : 텍스트 파일 : 엑셀 파일 : python 가공 을 부드럽게 연결해준다.**
    - **excel에서 불러오기** 위해서는 행 단위로 / , 를 통해서 구분해서 데이터를 입력한다.
    - **python에서 csv 모듈을 통해 가공**하기 위해서는 **CSV형 리스트(편의상 명명)**를 만들어준다.
    
```python
CSV형 리스트 = [[1행], [2행], [3행], ...]
// numpy module에서 배열을 정의하는 방식과 일치함
```

## 02. CSV reader, writer 정의
  - usecsv 모듈을 정의하여 CSV 파일을 불러오고 가공한다.

```python
# usecsv module

import csv, os

# filename은 .csv 확장자까지 지정해주어야 함
def opencsv(filename):
    
    # open()을 통해서 file을 'r'(읽기형식)로 불러들인다.  
    f = open(filename, 'r')
    
    # csv 파일을 행단위로 읽어들일 수 있게 하는 reader 객체를 생성한다.
    csvreader = csv.reader(f)
    
    # 행 단위로 읽어들인 내용을 저장할 비어있는 list를 생성한다.
    output = []
    
    # 행 단위로 추가한다.
    for i in csvreader:
        output.append(i)
    f.close()
        
    # CSV형 리스트를 출력한다.
    return output
    
def writecsv(filename, input_list):
  
    # 함수가 종료되면 close되도록 with 명령어 이용
    # newline='' 을 지정해주지 않으면, 행들이 한줄씩 띄어서 들어간다.
    with open(filename, 'w', newline='') as f:
        
        # file객체를 대상으로, csv.writer()를 통해서 csv 객체를 연다
        # , 로 끊어서 구분하여 넣는다.
        csvwriter = csv.writer(f, delimeter=',')
        
        # csv 객체에 list의 내용을 행단위로 입력한다.
        csvwriter.writerows(input_list) 
        
# test
if __name__ == "__main__":
    os.chdir(r'...')
    writecsv('practice.csv', [[1, 2], [2, 3, 4], [3, 4, 5]])
```

## 03. CSV 파일 가공
  - re module (정규표현식 관련 module)을 사용한다.
  - try: ~ except: 를 사용하여 예외를 처리한다.

### 1. ,가 포함된 문자열 수 -> 숫자형으로 바꾸기
  - 숫자만 있는 문자열 / 그렇지 않은 문자열을 구분 -> 숫자만 있는 문자열을 숫자형으로 바꾼다.
  - **re module**
    - **re(',', '', 문자열)** : 문자열 내의 ','를 공백으로 대체한다.
    - **re.search('\d', 문자열)** : 문자열 내에 숫자가 들어있다면 true 반환
    - **re.search('[a-z가-힣]', 문자열)** : 문자열 내에 알파벳이나, 한글이 들어있다면 true 반환
    - **re.search('[a-z가-힣!]', 문자열)** : 문자열 내에 알파벳, 한글, !(특수문자)이 들어있다면 true 반환
  - **try ~ except**
    - try , except를 통하여 int 형으로 바꿀 수 있는 경우만 변경할 수 있다. 

```python
import usecsv

input_list = usecsv.opencsv(...)

# input_list에 들어있는 , 포함된 문자열 숫자들을 숫자형으로 변경하기
for i in input_list:
    for j in i:
        if j == '' : continue
        if re.search('[a-z가-힣!]', j) : i[i.index(j)] = int(re.sub(',', '', j))

# try: except를 사용하면 훨씬 수월하다. 
for i in input_list:
    for j in i:
        try: i[i.index(j)] = int(re.sub(',', '', j))
        except: continue
```

  - **usecsv moudule에 switch함수 정의**
    - 리스트 안에 있는 문자열형의 숫자를 숫자형으로 바꾸는 switch 함수를 정의

```python
def switch(list_name):
    for i in list_name:
        for j in i:
            try : list_name[list_name.index(i)][i.index(j)] = int(re.sub(',', '', j))
            except : continue
    return list_name
```


