# 자료형

## 1. 숫자형 관련 연산

### 1.1 거듭제곱과 나눗셈 몫 구하는 연산

```python
# power
print(2**3)

# quotient
print(5//4)
```

## 2. 문자열 관련 연산

### 2.1 문자열을 만드는 4가지 방법
  - ' ', " ", ''' ''', """ """
  - 문자열에 ""있을 경우 '' 사용
  - 문자열에 ''있을 경우 "" 사용
  - (/) 써서 문자열 내의 ' "를 문자로 인식하게 만들 수 있다.

```python
# errstring = 'I'd like to play with you' 오류
string1 = "I'm Susan"
string2 = '"I love how it works"'
string3 = """
"what is your name?"
"My name is Jake"
"""
string4 = '''"maybe I'll see you again if there's another place
and if there ain't, well, it's been heaven known you"
'''
```

### 2.2 Concatenation(+), multiple Concatenation(*)
  - **\+ 연산은 두 문자열을 연결**시켜준다 (Concatenation)
    - 단, java 처럼 문자열 + 다른 타입 -> 문자열로 바꿔주지는 않는다.
    - **문자열 간에서만 + 연산이 지원된다.**
  - **\* 연산은 특정 문자열을 여러번 연결**시켜준다

```python
# Concatenation
str1 = "What "
str2 = "is "
str3 = "going on???"
print(str1 + str2 + str3)
print("Length of this sentence is " + str(len("Length of this sentence is ")))

# multiple concatenation
str4 = "Ha Ha Ha "
print(str4*3)
```

### 2.3 indexing, slicing, 문자열 수정
  - **indexing** : 문자열 내의 특정 문자 뽑아내기
    - 변수명[-n] : 뒤에서부터 n번째 문자를 뽑아낼 때 사용한다.

```python
# Indexing
a = "I'm gonna leave the door open"
print(a[0] + " " + a[1] + " " + a[2])
print(a[-4] + " " + a[-3] + " " + a[-2] + " " + a[-1])

# I ' m 
# o p e n
```

  - **slicing** : 문자열 내에서 특정 단어 뽑아내기
    - 변수명[시작 index : 끝 index] : [시작 index , 끝 index) 만큼의 문자들을 뽑아낸다

```python
# Slicing
a = "I'm gonna leave the door open"
print(a[0:3])
print(a[4:9])
print(a[-4:])

# I'm
# gonna
# open
```

  - **문자열 수정** : 문자열 자체는 immutable하기 때문에 인덱스로 접근하여 변경 불가능, 쪼개서 새로운 문자열을 생성해준다.

```python
a = "Breethless"
# a[3] = 'a' : 'str' object does not support item assignment, 문자열은 immutable 하기 때문에 변경 불가능
a = a[0:3] + 'a' + a[4:]
print(a)

# Breathless
```

### 2.4 formatting, 정렬, 공백, 소수점, format 함수
  - **formatting** : 문자열 내의 특정한 값을 바꿔줘야 하는 경우 사용

#### 2.4.1 % formatting 
  - %s %d %c %f %d %x %%(%를 format code로 인식하는 것을 방지)
  - %s는 어떤 형이든 문자열로 바꿔서 넣어준다.

```python
name = "Jackson"
number = 40
print("%s is in his early %s's" % (name, number) )

# number 40이 정수였어도 %s에 의해서 문자열로 들어간다.
```

  - **정렬과 공백**

```python
print("%-10s" %"Hi")
print("%10s" %"Hey")
print("%10s", "Hey")

"""
Hi        
       Hey
%10s Hey
"""
```

  - **소수점 표현**

```python
a = 4.5555555590
print("%25.12f" %a)

"""
           4.555555559000
"""
```

#### 2.4.2 format 함수
  - **{숫자} 인덱스 항목에** format 함수 내의 값(**리터럴, 문자열, 변수 등..**)을 넣어주는 방식
  - **{name} 항목에** format 함수 내의 값(**name = 리터럴, 문자열, 변수 등...**)을 넣어주는 방식
  - **{숫자: 정렬, 소수점 표현} 항목으로** 지정한 formatting 대상이 되는 부분에 들어가는 값의 정렬방식, 소수점 표현 방식을 지정
    
```python
print("I eat {0} apples".format("3"))
print("I eat {0} apples".format(3))

// 인덱스, name
number = 3
day = "three"
print("I eat {0} apples".format(number))
print("I eat {0} apples for {1} days".format(number, day))
print("I eat {number} apples. So I was sick for {day} days".format(number = 10, day = 4))

// 정렬
print("{0:>10}".format("JunL"))
print("{0:<10}".format("JunL"))
print("{0:^10}".format("JunL"))
print("{0:=^10}".format("JunL"))

// 소숫점 표현
x = 3.141592
print("{0:-15.12f}".format(x))

// format 함수와 중괄호
print({{}}.format())
```

#### 2.4.3 f 문자열 포매팅(3.6)
  - **문자열 안에 변수와 수식을 함께 사용하는 표현식을 허용**한다.

```python
# f 문자열 포매팅
# 1. 딕셔너리 : d[" "] d[' '] : 전체 문자열을 감싸는 따옴표가 무엇이냐에 따라서 달라진다.
d = {'name': 'lim', 'age': 30}
print(f"나의 이름은 {d['name']}입니다. 나이는 {d['age']}")

# 2. 정렬
print(f"{'abc':>10}")
print(f"{'abc':<10}")
print(f"{'ab':^10}")

# 3. 정렬과 공백 채우기
print(f"{'abc':!^11}")

# 4. 소수점 표현 (표현식 이용)
number = 3.14
print(f"{number + 3:10.4f}")

# 5. { } 표현
print(f"{{}}")
```

### 2.6 문자열 내장 함수
  - 문자열.count(특정 문자/ 문자열) : 문자열 내의 특정 문자나, 문자열의 갯수를 반환한다. "" 넣으면 길이+1 반환. 
    - len(문자열) : 문자열의 길이 반환 
  - 문자열.find() : 문자열 내의 특정 문자나, 문자열이 처음 등장한 위치(index)를 반환한다. 없으면 -1 반환.
  - 문자열.index() : 문자열 내의 특정 문자나, 문자열이 처음 등장한 위치(index)를 반환한다. 없으면 오류를 발생시킨다.
  - 문자열1.join(문자열2/리스트/튜플) : (문자열2/리스트/튜플) 내의 각 문자들 사이에 문자열1을 끼워 넣는다
  - 문자열.upper() : 문자열 내의 모든 문자들을 대문자로 바꾼다
  - 문자열.lower() : 문자열 내의 모든 문자들을 소문자로 바꾼다
  - 문자열.lstrip() : 문자열 내의 왼쪽에 존재하는, 첫 공백 이외의 문자가 등장할때까지의, 공백을 제거한다.
  - 문자열.rstrip() : 문자열 내의 오른쪽에 존재하는, 첫 공백 이외의 문자가 등장할때까지의, 공백을 제거한다.
  - 문자열.strip() : 문자열 내의 오른쪽 왼쪽에 존재하는, 첫 공백 이외의 문자가 등장할때까지의, 공백을 제거한다.
  - 문자열.replace(문자열1, 문자열2) : 문자열 내에 있는 모든 문자열1을 문자열2로 바꾼다.
  - 문자열.split(문자열1) : 문자열을 문자열1을 기준으로 쪼개서 리스트를 만든다. 문자열1에 아무것도 제공하지 않으면 공백(space, tab, enter)을 기준으로 쪼갠다.

### !!!python!!! 출력

```python
# !!!python!!! 출력하기
name = "python"
print("!"*3 + "%s" % "python" + "!"*3)
print("{0}".format("!!!python!!!"))
print("{0:!^12}".format("python"))
print("{name}".format(name = "!!!python!!!"))
print("{name:!^12}".format(name = "python"))
print("{name:!^12}".format(name = name))
print(f"{'python':!^12}")
```






