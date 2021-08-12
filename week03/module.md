# Module
  - 함수나, 변수, 혹은 클래스들을 모아놓은 파일이다.
  - 다른 파이썬 프로그램에서 불러와 사용할 수 있도록 구성한 파일 덩어리
  - 이미 만들어 놓은 모듈을 사용하거나, 내가 모듈을 만들어 사용 가능


## 01. terminal 환경, module 사용

### 1. '.py' python file을 만든다

```python
# ModuleTest.py

PI = 3.141592
class Circle:
    def AreaOfCircle(self, r):
        return (r ** 2) * PI
    def PerimeterOfCircle(self, r):
        return (r * 2) * PI

def add(a, b):
    return a+b

def sub(a,b):
    return a-b

def abssub(a,b):
    return a-b if a>b else b-a
```

### 2. '.py' 확장자의 module이 저장되어 있는 디렉토리로 이동한다.
  - cd : 디렉터리 위치 이동
      - cd directory명 : 하위 디렉터리 이동
      - cd .. : 상위 디렉터리 이동
      - cd / : 최상위 디렉터리 이동
  - pwd : 현재 디렉터리 위치 확인
  - ls : 현재 디렉터리에 존재하는 파일 확인

### 3. python 대화형 인터프리터 실행
  - 명령어 'python'으로 실행

### 4. module을 import하여 내부에 정의된 함수, 변수, 클래스들을 사용한다
  - import module명
  - from module명 import module내 function
    - from module명 import * : module 내부 전체 import
    - from module명 import n, m, ,, : 특정한 부분들만 import
    - from module명 import n : 특정한 부분만 import

<img src="https://user-images.githubusercontent.com/59442344/129163800-201057df-7ef6-4dbf-93f4-89b56074a6e3.png" width="40%" height ="40%">

<img src="https://user-images.githubusercontent.com/59442344/129175700-d760db01-4fd7-4ce0-adf0-870dac510944.png" width="40%" height ="40%">


## 02. import vs 직접 실행
  - python file을 작성할 때, 해당 파일 import시에 파일 내의 특정 부분이 실행되지 않도록 \_\_name__ 변수를 통해서 설정할 수 있다.
  - \_\_name__ 변수
    - python 파일들마다 존재하는 변수
    - **해당 파일이 import된 경우**, 해당 파일의 **\_\_name__ 변수에 "해당 파일명"이 들어간다.**
    - **해당 파일이 직접 실행된 경우**, 해당 파일의 **\_\_name__ 변수에 "\_\_main__ "이 들어간다.**

```python
# ModuleTest.py

def add(a, b):
    return a+b

def sub(a,b):
    return a-b

def abssub(a,b):
    return a-b if a>b else b-a

if __name__ == "__main__":
    print("File running now")
```


