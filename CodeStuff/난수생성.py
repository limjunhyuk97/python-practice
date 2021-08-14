## 난수 생성 : random module import

import random

n = int(input())

for _ in range(n):
    r = random.randint(1, 10)
    print(r)
