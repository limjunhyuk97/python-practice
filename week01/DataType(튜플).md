# 튜플
  - 리스트는 요소를 변경할 수 있고, **튜플은 요소를 변경/삭제 할 수 없다.**
  - 리스트는 [ ]로 감싸지만, 튜플은 ( )로 감싼다.
  - 튜플은 요소의 수를 사전에 정확히 알고 있을 때 사용하며, 각 요소의 위치가 큰 의미를 갖고 있다.
  - tuple(리스트) : 리스트 -> 튜플 변경 가능

## 01. 튜플 생성
  - 하나의 요소를 넣어줄 때는 끝에 , 를 붙여야 한다.
  - ( )의 괄호를 생략할 수 있다.

```python
t1 = ()
t2 = (1,)
t3 = (3, 4, 5)
t4 = (3, 4, ("abs", 'bc', 3), 6, ("ab"))

print(t4[4:5])
# ('ab',)
```

## 02. 튜플 indexing

```python
Tuple = (1, 4, 6, ("what", "am", "I"), 2, ("Supposed", "to", "do", 10), 5)

print(Tuple[3])
# ('what', 'am', 'I')
```


## 03. 튜플 slicing

```python
Tuple = (1, 4, 6, ("what", "am", "I"), 2, ("Supposed", "to", "do", 10), 5)

print(Tuple[3:4])
print(Tuple[0:1])
# (('what', 'am', 'I'),)
# (1,)
```


## 04. 튜플 연산 및 길이
  - 튜플 요소의 삭제/변경은 불가능 하지만, **튜플끼리 더하거나, 곱하는 연산은 허용**

```python
Tuple = (1, 2, 3)

Tuple = Tuple + Tuple
print(Tuple)
# (1, 2, 3, 1, 2, 3)

Tuple *= 2
print(Tuple)
# (1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3)

print(len(Tuple))
# 12
```

## 05. Named Tuple
  - 튜플의 각 요소(위치)의 의미를 명시적으로 작성할 수 있다

```python
from collections import namedtuple
Physical = namedtuple("Physical", "Height, Weight, Name, Age")
Tom = Physical(183, 78, "Tom", 25)
Jack = Physical(190, 79, "Jack", 24)

print(Tom.Height)
# 183
```
