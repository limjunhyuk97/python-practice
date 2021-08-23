# int() : 10진수 문자열 -> n진수
print(int('13', 16))
print(int('13'))
print(int('11', 2))
print(int('12', 8))


# bin(), hex(), oct() : n진수 -> n진수 문자열
print(bin(0xa1))
print(hex(0o76))
print(oct(0b1101))
print(str(0xa1))
## 0b10100001  0x3e  0o15  161
## str(특정진수 문자열) : 10진수로 바꿔서 문자열 출력


# format() 내장 함수
print(format(10, '#b'))
print(format(10, '#d'))
print(format(10, '#o'))
print(format(10, '#x'))
print("{0:#b}, {0:#d}, {0:#o}, {0:#x}".format(10))
## 0b1010  10  0o12  0xa


# 입력 문자열 실수 변환 -> float()
print(float('3.14') + 0.09)

# 10진수 -> n 진법 변환
def card_conv(x : int, r : int) -> str:
    d = ''
    dchar = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    while x > 0 :
        d += dchar[x % r]
        x //= r
    return d[::-1]
