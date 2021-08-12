# Function

## 1. 함수 정의
  - **def 함수명(매개인자, 매개인자, ,,):**
  - **def 함수명(\*매개인자):**
    - 몇개의 인자가 전달된 지 모를 때의 선언 방식
    - \*을 붙이면, 전달된 인자들이 묶여서 tuple이 된다.
  - **def 함수명(\*\*매개인자):**
    - 몇개의 인자가 전달될 지 모를 때의 선언 방식
    - \*\*를 붙이면, 전달된 a=b 형식의 인자들이 묶여서 dictionary가 된다.
    - **키워드 파라미터**라고 한다.

```python
# 1. def 함수명(*args):

def multi_operation(key, *args):
    if key == 'add':
        sum = 0
        for num in args:
            sum += num
        print(sum)
    elif key == 'multiply':
        sum = 1
        for num in args:
            sum *= num
        print(sum)

print(multi_operation('multiply', 1, 2, 3, 4, 5))
## 120


# 2. def 함수명(**args):

def makeDict(**args):
    return args

dict = makeDict(a = 1 , b = 2)
print(dict)
## {'a': 1, 'b': 2}
```

## 2. 함수 결과값은 언제나 하나.
  - return 문을 만나면 함수는 종료되고, 실행흐름이 함수를 빠져나가게 된다.
  - return n, m, ,,, : 여러 개의 결과 값들이 tuple 형식으로 전달된다.

```python
# 함수 결과값은 하나
def function(a, b):
    return a+b, a*b, a//b, a%b

print(function(10,3))
## (13, 30, 3, 1)
```

## 3. 매개변수 초기값 설정 가능
  - cpp에서의 디폴트 매개변수와 비슷한 기능이다.
  - 초기화 값을 부여할 매개변수는 오른쪽부터 선언해야 한다.

```python
# 매개변수 초기화, 디폴트 매개변수
def add(m = 10, n =2):
    return m + n

print(add())
## 12

# 오른쪽 부터 디폴트 매개변수 지정을 해줘야 한다.
def add(m = 10, n):
    return m + n

## SyntaxError: non-default argument follows default argument
```

## 4. 함수 내부에서 선언한 변수는 함수 내에서만 머무른다.
  - 함수 외부에 있는 변수명과 겹친다면, 함수 내부에서는 내부에서 선언된 변수로 사용된다.
  - global을 선언해주면, 외부에 선언된 변수를 끌어와 쓸 수 있으나, 좋지 못하다.`

```python
# 변수의 효력 범위

a = 10
def add(a):
    a += 1
    return a
print(add(a), a)
## 11 10
```

# Lambda Expression
  - lambda n, m, ,, : 표현식(반환값을 만든다)
  - def보다 간결한 함수 표현 방식

```pyhton
# Lambda
absSubtract = lambda x, y : x - y if x > y else y - x
print(absSubtract(10, 6))
print(absSubtract(3, 9))
## 4
## 6
```

