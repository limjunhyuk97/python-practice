# Iterable
  
## Iterable 객체
  - 내부 요소들에 대해서 순차적으로 접근이 가능한 객체를 의미한다. (for문에 넣어 돌릴 수 있음을 의미한다.)
  - iterable한 객체는 iterator 객체를 얻을 수 있는 객체를 의미한다.
    - **iterable 객체를 대상으로 iter()함수를 호출하여 iterator 객체를 생성하면, 요소들에 대한 순차 접근이 가능해진다.**
    - **iterator 객체에 대하여 next()함수를 사용하여 요소들에 차례대로 접근이 가능해진다.**
  - **list, tuple, dictionary, set, str(string), bytes, range** 타입이 iterable한 타입에 해당한다.

```python
dict = {1:2, 3:4, 5:6}

iter_Dict = iter(dict)
print(next(iter_Dict))
print(next(iter_Dict))
print(next(iter_Dict))
print(next(iter_Dict))

## 1 3 5 StopIteration
```

