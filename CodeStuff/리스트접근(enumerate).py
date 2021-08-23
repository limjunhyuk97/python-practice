arr = [3, 4, 'Tom', 'Jack', 'Jane', 6, 7]

for i in range(len(arr)):
    print(arr[i],' ', end='')
print()

## enumerate(list) : list, tuple 내 원소들에 대해서 (index, value)의 tuple 쌍을 만든다.
for i, el in enumerate(arr):
    print(i, ':', el,' ', end='')
print()

for i, el in enumerate(arr, 1):
    print(i, ':', el,' ', end='')
print()

for i in arr:
    print(i,' ', end='')
print()
