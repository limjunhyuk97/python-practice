# from math import pi, ceil as c
# import pyautogui as pg
#
# print(pi)
# print(c(2.7))
#
# pg.moveTo(500, 500, duration= 2)

version = 2.0

def printAuthor():
    print("author....")

class Pay:
    def __init__(self, id, price, time):
        self.id = id
        self.price = price
        self.time = time
    def get_pay_info(self):
        return f"{self.time} {self.id} {self.price}"

if __name__ == "__main__":
    print("main 으로 실행")

print(__name__)