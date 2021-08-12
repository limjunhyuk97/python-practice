# File IO

## File 입출력
  - file 생성 및 작성 : open('파일 경로', 'w')
  - file 읽어들이기 : open('파일 경로', 'r')
  - file 내용 추가 : open('파일 경로', 'a')

```python
# file 입력

## 1. write()
fw = open('...', 'w')
for i in range(1, 11):
    data = f"{i} line.\n"
    fw.write(data)
fw.close()

# file 출력

## 1. readline() : line 단위로 file에 읽어들인다
fr = open('...', 'r')
while True:
    line = fr.readline()
    if not line: break
    print(line, end='')
fr.close()

## 2. readlines() : 전체 line을 읽어서 리스트로 반환해준다.
fr = open('...', 'r')
lines = fr.readlines()
for line in lines:
    print(line, end='')
fr.close()

## 3. read() : 파일 전체의 내용을 문자열로 돌려준다
fr = open('...', 'r')
all = fr.read()
print(all)
fr.close()

# file 내용추가

## 1. write()
fa = open('...', 'a')
for i in range(11, 21):
    fa.write("%d line.\n" %i)
fa.close()
```

## File 객체 자동 close (with 문)
  - with open(...) as 객체명:

```python
# with 문을 사용한 파일 객체 자동 소멸
with open('...', 'r') as f:
    lines = f.readlines()
    for i in range(len(lines)):
        print(lines[i], end = '')
```

## 프롬프트 실행
  - **sys 모듈**을 사용하여 **프롬프트에서 매개변수(pyhton 파일명, 파일에 제공할 인수)를 전달**하여 **python 파일 실행**시키기

```python
import sys
args = sys.argv[1:]
for i in args:
    print(i)
```

