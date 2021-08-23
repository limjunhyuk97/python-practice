# N개 중 가장 큰 값

## 0. 함수 구현
def maxN(*args):
    max = 0
    for num in args:
        if max <= num:
            max = num
    return max

print(maxN(2,3,4,5,6))

## 1. 함수 구현
import random
from typing import Any, Sequence

def max_of(a : Sequence) -> Any:
    maximum = a[0]
    for i in range(len(a)):
        if maximum < a[i]:
            maximum = a[i]
    return maximum

if __name__ == '__main__':
    print('배열의 최대값을 구합니다.')
    num = int(input('원소 수를 입력 하세요 : '))
    x = [None] * num

    for i in range(num):
        x[i] = random.randint(0, 200)
        print(x[i], ' ', end='')

    print(f'\n최대값은 {max_of(x)} 입니다.')


    
    
# min / max 함수 + 'key=' 조건 이용하기

## 1. 리스트에서 최대값 / 최소값
list = [2, 3, 4, 5, 6, 7, 8]
print(max(list))
print(min(list))
print(max([num for num in range(1, 20)], key = lambda x : x % 4 and x))
## 8 2 19


## 2. 딕셔너리에서 최대 value key / 최소 value key
dict = {1:10, 2: 20, 3: 30, 4:23, 5: 9}
print(max(dict, key = dict.__getitem__))
print(min(dict, key = dict.__getitem__))
## 3 5

### __getitem__ : 특정 객체내의 요소들을 슬라이싱하기 위한 메소드이다.
### max, min 에서의 key : key로 넣은 기준으로 max, min 값을 도출해 낸다.
