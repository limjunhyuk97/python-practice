# Control Statement


## If

### 1. pass 와 continue
  - pass는 단순히 실행시킬 내용이 없음을 의미
    - 조건문에서 별도로 부여할 조건의 따로 없을 때
    - class 생성 시에 초기에 넣어줄 값이 따로 없을 때  
  - continue는 다음 loop 단계로 넘어가도록 한다

```python
for i in range(10):
    if i % 2 == 0:
        pass
        print(i, end = ' ')
    else:
        continue
        print(i, end = ' ')
print("Done")

# 0 2 4 6 8 Done
```

### 2. Conditional Expression
  - ...를 if ...일 때 실행시키고, else 일 때 ... 실행시켜라

```python
score = 95
print("A") if score >= 80 else print("B")

# A
```
 
## While
  - while 조건 :

### 1. Example
  - while 문 사용 예시

```python
# 0 부터 9까지 출력

DOIT = 0
while DOIT < 10:
    print(str(DOIT) + " turn")
    DOIT += 1

# 커피 자판기
print("\nCoffee machine")
MSG = "insert coin : "

coffee = 5; money = 0
while coffee > 0:
    print(MSG, end = "")
    money = int(input())
    if money > 300:
        print("change : {change}, and here's your coffee".format(change = money - 300))
    elif money == 300:
        print("Here's your coffee")
    else:
        print("Not enough money!")
    coffee -= 1    
```

## For
  - for 변수 in 'list, tuple, string, dictionary(key value), set'
  - 변수를 리스트나 튜플형식으로 설정하여, 여러 개의 값을 동시에 받을 수 있다.

### 1. Example










