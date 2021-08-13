# N개 중 가장 큰 값
# N개 중 가장 큰 값

## 함수 구현
def maxN(*args):
    max = 0
    for num in args:
        if max <= num:
            max = num
    return max

print(maxN(2,3,4,5,6))

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
### max, min 에서의 key : 정렬의 기준을 사용자가 설정할 수 있게 해준다.
