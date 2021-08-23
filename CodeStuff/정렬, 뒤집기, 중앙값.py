# 리스트 sorting과 중앙값 찾기

'''
## sorting 방식

1. list.sort()
    - list를 sorting한다.

2. sorted(list)
    - sorting된 list를 반환한다.
    - 기존의 list는 sorting되지 않는다.

## sorting Parameter
3. key
    - 정렬이 되는 기준을 설정한다.

4. reverse
    - reverse=True 설정은 역순(내림차순)으로 정렬을 유도한다.

## 뒤집기

1. list.reverse()
  - list를 역순으로 정렬
  
2. reverse(list)
  - list 원소를 역순으로 꺼내는 iterable 객체를 생성
'''


## 중앙값 찾기
def list_mid(*args):
    List = sorted(list(args))
    return List[len(List) // 2] if len(List) % 2 == 1 else (List[len(List)//2-1], List[len(List)//2])

print(list_mid(3, 1, 6, 10, 54,222, 8, 7, 34, 22))


## list 역순 정렬
from typing import Any, MutableSequence

def reverse_list(arr: MutableSequence) -> None:
    for i in range(len(arr) // 2):
        arr[i], arr[len(arr) - i - 1] = arr[len(arr) - i - 1], arr[i]
