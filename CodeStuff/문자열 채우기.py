## 문자열 앞부분부터 0 또는 원하는 단일문자로 채우는 방법

# zfill
print("".join(['hi', 'there', 'haha']).zfill(15))

# rjust
print("".join(['hi', 'there', 'haha']).rjust(15, "a"))
