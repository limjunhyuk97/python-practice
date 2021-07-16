# Dictionary
  - **Key-Value 쌍으로 이루어진 자료형**을 Hash, Associative array라 하는데, **파이썬에서는 Dictionary라는 이름으로 이를 구현**한다.
  - list와 tuple과는 다르게, **sequential하게 요소를 찾지 않는, unordered 자료형이다.** 즉, **key 값으로 요소에 접근**한다.
  - 어떤 **key 값이 갖는 value에 대해서 빠른 접근**이 요구될 때, **key 값으로 바로 value에 접근**하고자 할 때 사용한다.
  - **key 값은 고유해야 한다.**

## 01. 생성
  - **{ } 속**에 **Key : Value로 이루어진 쌍 여러 개**를 집어 넣는다.
   - **Key 에는 immutable 자료형** 사용 : **Tuple, String, Number**
   - **Value 에는 immutable 또는 mutable 자료형** 사용 : **Tuple, String, Number, List, Dictionary, Set**

```python
class1 = {'Bachelor' : ['Tom', 'Jack', 'Anna', 'Bill'], 'Master': ['Ronny', 'Chris']}
print(class1['Bachellor'][0])

class2 = {(1, 2, 3) : ['ABC', 2], ('KDA', 'DOC', 2) : 3}
print(class2[(1,2,3)])

# Tom 
# ['ABC', 2]
```

## 02. 요소 추가
  - **Dictionary명[key] = value**
  - sequential한 자료구조가 아니기 때문에, 뒤에 append한다는 개념이 없다.

```python
class2 = {(1, 2, 3) : ['ABC', 2], ('KDA', 'DOC', 2) : 3}

class2[3] = 6
print(class2)

# {(1, 2, 3): ['ABC', 2], ('KDA', 'DOC', 2): 3, 3: 6}
```

## 03. 요소 삭제
  - **del Dictionary명[key]** : key 값에 대해서 key-value 쌍을 삭제
  - **Dictionary명.pop(key, default)** : dictionary에서 key를 제거하고, key값과 쌍을 이루는 value 값을 반환. key 값이 없다면 default 값 반환

```python
class2 = {(1, 2, 3) : ['ABC', 2], ('KDA', 'DOC', 2) : 3}

del class2[(1,2,3)]
print(class2)

# {('KDA', 'DOC', 2): 3, 3: 6}
```

## 04. 요소 접근
  - **Dictionary명[key]** : 이를 통해서 key와 쌍으로 연결되어 있는 value에 접근
    - 여기서 key 값은 index가 아니다! **그냥 key 값 그 자체로 탐색**하는 것이다. : 
    - **key 값이 없으면 오류를 생성**한다.
    - key 값이 중복되어 사용되면 안된다. 만약에 중복되어 사용되었다면, 마지막 key-value 쌍이 사용된다.

```python
dictionary = {1 : '1234', 2: '2345', 3: '3456'}
print(dictionary[1] , dictionary[2])

# 1234 2345
```

## 05. Dictionary 관련 함수
  - **.keys()** : 해당 dictionary가 가지고 있는 key들을 모아서 **dict_keys 객체로 반환**해준다.
    - **dict_keys, dict_values, dict_items 객체들은 리스트가 아니다** : **append, insert, pop, remove, sort 이용 불가능**
    - list() 함수를 이용하여 list로 변환시켜준다면 위의 기능들을 사용할 수 있다.
    - **list로 변환시키지 않더라도 반복구문을 사용**할 수는 있다.
  - **.values()** : 해당 dictionary가 가지고 있는 value들을 모아서 **dict_values 객체로 반환**해준다.
    - 마찬가지로 dict_values 객체는 list가 아니다.
  - **.items()** : 해당 dictionary가 가지고 있는 key-value쌍들을 모아서 **dict_items 객체로 반환**해준다.
    - 이또한 list가 아니다

```python
dictionary = {1: '1234', 2: '2345', 3: '3456', 'kim': 23, 'Lim':25}

dictionary_Key = dictionary.keys()
print(dictionary_Key)

dictionary_Values = dictionary.values()
print(dictionary_Values)

dictionary_Items = dictionary.items()
print(dictionary_Items)

# dict_keys([1, 2, 3, 'kim', 'Lim'])
# dict_values(['1234', '2345', '3456', 23, 25])
dict_items([(1, '1234'), (2, '2345'), (3, '3456'), ('kim', 23), ('Lim', 25)])
```

  - **.clear()** : 해당 dictionary의 모든 요소를 삭제한다.
    - **.clear()** vs **dict() , {}**
    - **.clear()** 는 해당 변수가 가리키는 객체의 모든 요소들을 삭제하는 것이다!
      - 변수가 가리키던 해당 dictionary 내의 key, value, key-value 쌍 등의 객체들이 사라진다.
    - **dict(), {}** 는 해당 변수에게 빈 dictionary를 할당시켜준다.
      - 변수가 가리키던 해당 dictionary 내의 key, value, key-value 쌍 등의 객체들은 아직 남아있다.
      - 단지, 변수가 요소가 없는 새로운 {} dictionary를 가리키게 된 것 뿐이다.

```python
dictionary = {1: '1234', 2: '2345', 3: '3456', 'kim': 23, 'Lim':25}
dictionary_Items = dictionary.items()

# case 1
dictionary.clear()
print(dictionary)
print(dictionary_Items)
# {}
# dict_items([])

# case 2 
dictionary = dict()
print(dictionary)
print(dictionary_Items)
# {}
# dict_items([(1, '1234'), (2, '2345'), (3, '3456'), ('kim', 23), ('Lim', 25)])
```

  - **.get(key)** : key와 쌍을 이루는 value를 반환한다.
    - .get()은 해당 key가 없으면 None을 반환한다
    - Dictionary명[key]에 해당 key가 없으면 오류를 반환한다.  
    - **.get(key, default)** 를 사용하면 **key가 없는 경우 default 값을 반환**한다.

```python
dictionary = {1: '1234', 2: '2345', 3: '3456', 'kim': 23, 'Lim':25}

print(dictionary.get(5))
print(dictionary.get(5, -1))
# None
# -1
```

  - **key in dictionary명** : key가 dictionary에 있으면 true, 없으면 false

```python
dictionary = {1: "bad", 2: "not bad", 3: "good", 4: "outstanding"}
print(1 in dictionary)
print(6 in dictionary)

# true
# false
```
