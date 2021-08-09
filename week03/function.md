# Function

## 1. 함수 정의
  - **def 함수명(매개인자, 매개인자, ,,):**
  - **def 함수명(\*매개인자):**
    - 몇개의 인자가 전달된 지 모를 때의 선언 방식
    - \*을 붙이면, 전달된 인자들이 묶여서 tuple이 된다.
  - **def 함수명(\*\*매개인자):**
    - 몇개의 인자가 전달될 지 모를 때의 선언 방식
    - \*\*를 붙이면, 전달된 a=b 형식의 인자들이 묶여서 dictionary가 된다.
    - **'키워드 파라미터'**라고 한다.

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
  - return 문을 만나면 함수는 종료되고, 실행흐름이 함수를 빠져나가게 된다
  - return n, m, ,,, : 여러 개으 
  - return 문을 만나면 함수는 종료되고, 실행흐름이 함수를 빠져나가게 된





