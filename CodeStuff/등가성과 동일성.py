# 등가성(Equality)과 동일성(Identity)

import copy

list1 = [[1,2],3]
list2 = copy.deepcopy(list1)

print(list1 == list2)
print(list1 is list2)

## 등가성 : 값이 같은지 비교 : ==
## 동일성 : 같은 객체인지 비교 : is
