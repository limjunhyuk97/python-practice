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
  - **range(a,b) 함수**를 사용하면 a 이상 b 미만의 정수를 포함하는 range 객체를 만들 수 있다.

### 1. Example

```python
# 구구단
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{j:^3} * {i:^3} = {i * j:^8}", end=" ")
    print()

# 성적산출 : 60점 초과하는 성적만 통과
marks = [90, 45, 60, 72, 89, 100, 45, 23, 30, 55]
for number in range(len(marks)):
    if marks[number] <= 60: continue
    print(f"student {number + 1}. Congratulations, you pass the exam with score : {marks[number]}")
```

  - **list 내포**
    - '표현식(항목과 관련된)' **for** '항목' **in** '반복 가능 객체' **if** '조건'
    
### 2. Example

```python
# 리스트 내포 사용하기
list = [2, 3, 5, 6, 8, 1, 4, 3, 6]
list2 = [num * 4 for num in list if num * 4 >= 20]
print(list2)

list2 = [num * 4 for num in list if num * 4 < 20]
print(list2)

```







