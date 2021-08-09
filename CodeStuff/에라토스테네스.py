# 1 ~ n 까지의 수 중에서 소수를 찾아 list로 반환한다

def PrimeNumber(n):
    primeCheck = [True for i in range(n+1)]
    for i in range(2, int(math.sqrt(n+1)) + 1):
        if primeCheck[i]:
            j = 2
            while i * j <= n:
                primeCheck[i*j] = False
                j += 1
    return [i for i in range(2, n+1) if primeCheck[i] ]
