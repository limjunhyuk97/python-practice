# Set
  - Dictionary와는 다르게 key-value 쌍으로 이루어져 있지 않으며, **수학에서의 집합과 유사**하다.
  - unordered하므로 **index를 활용하여 sequential하게 요소를 찾지 않는다.**
  - 각 **value 값은 고유**해야 한다 : **list, string, tuple 내부의 중복값 제거에 이용 가능**하다.
  - **set은 mutable** 하지만, set **내부 value들은 hashable** 해야한다.
    - number, string, tuple, boolean  O
    - list, dictionary, set X

## 생성
  - { ... } : 중괄호로 감싸서 생성
  - **set() 함수**로 set를 생성
    - set([ ... ]) : set() 내부에 리스트로 제공
    - set(" ... ") : set() 내부에 문자열로 제공
    - set(( ... )) : set() 내부에 튜플로 

```python
Set1 = {1, 2, 3}
Set2 = set([1, 2, 3])
Set3 = set("1294323")

print(Set3)
# 4 2 9 3 1
```

## 접근
  - unordered하기 때문에 []를 사용하여 index로 접근할 수 없다.
  - list(), tuple()을 이용하여 set를 list나 tuple로 변경하여 []를 사용하여 index로 접근할 수 있다.

```python
Set3 = set("1294323")

list3 = list(Set3)
print(list3[2])
# 3

tuple3 = tuple(Set3)
print(tuple3)
# ('4', '2', '9', '3', '1')
```

## 집합 연산
  - 교집합, 합집합, 차집합, 대칭 차집합
    - &, intersection
    - |, union
    - \-, difference
    - ^, symmetric_difference

```python
Set1 = {1, 2, 3, 4, 5, 6}
Set2 = {4, 5, 6, 7, 8, 9}

# 교집합
print(Set1 & Set2)
print(Set1.intersection(Set2))

# 합집합
print(Set1 | Set2)
print(Set1.union(Set2))

# 차집합
print(Set1 - Set2)
print(Set1.difference(Set2))

# 대칭 차집합
print(Set1 ^ Set2)
print(Set1.symmetric_difference(Set2))
```

## 함수
  - **요소 in set** : 요소가 set 안에 있으면 true, 없으면 false
  - **set.add(immutable한 요소)** : **immutable한 자료형**의 **요소 한덩어리**를 set안에 전달할 수 있다.
  - **set.update(mutable한 요소)** : **mutable한 자료형**을 통해서 **여러 요소**를 set안에 전달할 수 있다.
  - **set.remove(요소)** : 요소가 set 안에 있으면 제거, 없으면 오류 생성
  - **set.discard(요소)** : 요소가 set 안에 있으면 제거, 없어도 오류 생성하지 않음
  - set1.issubset(set2) : set1이 set2의 부분집합이면 true
  - set1.superset(set2) : set1이 set2을 포함하는 집합이면 true
  - set1.isdisjoint(set2) : set1과 set2의 공통원소가 없으면 true

```python
Set1 = set((1, 2, 3))
print(Set1)
# {1, 2, 3}

Set1.add((4, 5, 6))
print(Set1)
# {1, 2, 3, (4, 5, 6)}

Set1.update({14, 16})
print(Set1)
# {16, 1, 2, 3, (4, 5, 6), 14}

Set1.add("187")
print(Set1)
# {16, 1, 2, 3, (4, 5, 6), '187', 14}
```

