# Class

## Class 생성

### 1. 빈 껍데기 class

```python
class Empty:
  pass
```

### 2. 생성자 : 객체 생성 시에 자동으로 호출된다.
  - def __init__(self, 매개변수...)
  - 객체 생성 시에 자동으로 호출되는 메소드이다.

### 3. 메서드 : self, 매개인자1, 매개인자2,,
  - 메서드 선언 시 첫번째 매개변수 위치에, 어떤 객체에 인자들을 전달할 지에 대한 내용을 선언한다.
  - **def 클래스**.이름.메서드() 형태로 호출 시에는 객체명 명시해야 한다.
  - **def 객체명**.이름.메서드() 형태로 호출 시에는 객체명 명시 생략 가능하다.

### 4. 객체 변수, 클래스 변수
  - **객체 변수**
    - java, cpp 와는 다르게 미리 필드(멤버 변수)를 선언해 놓지 않아도, 메서드(혹은 생성자) 내에서 객체 내에 존재하지 않던 변수에 대한 내용을 다루면, 알아서 객체 변수가 생성 및 초기화 된다.
    - class틀을 바탕으로 찍어낸 특정 객체에게만 속한 변수이다.
  - **클래스 변수**
    - class에 속하는 변수로, 특정 class를 바탕으로 찍어낸 객체들이 공유한는 변수이다. (java의 static field같은 느낌이다.) 

```python
class FourCal:
    # class 변수
    first = 0
    second = 0
    
    # 메서드
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setData(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        return self.first + self.second
    def sub(self):
        result = self.first - self.second
        return result
    def mul(self):
        return self.first * self.second
    def div(self):
        return self.first / self.second

cal = FourCal(2, 3)
print(cal.sub())
# -1

print(cal.first, FourCal.first)
# 2(객체 변수 출력) 0(class 변수 출력)
```

# 상속
  - cpp, java 에서와 마찬가지로, 기존 class 기능의 확장을 용이하게 해주고, 코드의 재사용성을 높이기 위해 사용한다.
  - class class명(super class) : super class를 상속
  - 생성자
    - 상위 class.__init__(self, 전달 인자..)
    - super().__init___(전달인자..)

```python
class Car:
    tire = ""
    engine = 0
    def __init__(self, tire, engine):
        self.tire = tire
        self.engine = engine
    def fuelEfficiency(self):
        print(self.engine.efficiency())

class Engine:
    CC = 0
    def __init__(self, CC):
        self.CC = CC
    def efficiency(self):
        return self.CC

class TurboEngine(Engine):
    decreaseRate = 0
    def __init__(self, CC, decreaseRate):
        Engine.__init__(self, CC)
        # super().__init__(CC)
        self.decreaseRate = decreaseRate
    def efficiency(self):
        return self.CC * self.decreaseRate


car1 = Car("Kumho", TurboEngine(1500, 0.8))
car1.fuelEfficiency()
```

