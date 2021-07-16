# Code Stuff

## 1. list pop

```python
a = [1, 2, 3, 4]
while a:
  print(a.pop())
```

## 2. 중복 제거

```python
list1 = [2, 3, 2, 3, "string", "string", True, True, False]
tuple1 = (2, 3, 2, 3, 5, 6, 6, 6)
print(list(set(list1)))
print(tuple(set(tuple1)))

# [False, True, 2, 3, 'string']
# (2, 3, 5, 6)
```

## 3. join()의 사용

```python
# tuple, list, set에 대해서
string1 = "To be or not to be"
print("".join(('12', '34')))
print("".join(['12', '34']))
print("".join({'12', '34'}))
print("".join(set(string1)))

# 1234 1234 1234
# oT trben
```

## 4. swap

```python
a, b = [1, 2, 3], (2, 4)
a, b = b, a
print(a)
print(b)

# (2, 4)
# [1, 2, 3]
```
