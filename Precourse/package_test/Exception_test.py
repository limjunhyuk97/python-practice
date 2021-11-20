won = input("원화금액 입력 : ")
dollar = input("환율 입력 : ")

try:
    print(int(won)/int(dollar))
except ValueError:
    print("Value Error occured")
except ZeroDivisionError:
    print("Zero Division Error occured")

# 예외만들기
class PositiveNumberError(Exception):
    def __init__(self):
        super().__init__("양수는 입력불가능")

# raise : 강제로 예외를 만든다.

try:
    num = int(input("음수를 입력 : "))
    if num >= 0 :
        raise PositiveNumberError
except PositiveNumberError as e:
    print(e)
