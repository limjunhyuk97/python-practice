import random

print("================== class 사용")

# 기본 class
class Monster:
    max_monster_num = 1000
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
        # 클래스 변수에 대해 접근할 때 사용하는 방식
        Monster.max_monster_num -= 1
    def basic_attack(self):
        print(f"{self.name} , 공격력 : {self.attack}")
    def decrease_health(self, num):
        self.health -= num
    def get_health(self):
        return self.health
    def move(self):
        print("move!")

# 유도 class
class Wolf(Monster):
    pass

class Shark(Monster):
    def move(self):
        print("swim")

class Dragon(Monster):
    ## 클래스 변수 : 인스턴스 들이 모두 공유하는 변수
    skills = ("fire", "tail", "hit")
    def __init__(self, name, health, attack):
        ## super()를 통해서 기초 class 내에 존재하는 변수, 메소드 들에 접근할 수 있다.
        super().__init__(name, health, attack)
    def move(self):
        print("fly!")
    def skill(self):
        print(f"{self.name} used skill! {self.skills[random.randint(0, 2)]}")

dragon = Dragon("dragon", 100, 50)
dragon.skill()
print(Monster.max_monster_num)

wolf = Wolf("wolf", 2000, 30)
print(Monster.max_monster_num)

print("================== class 예시")
class Item:
    def __init__(self, name, price, weight, isdropable):
        self.name = name
        self.price = price
        self.weight = weight
        self.isdropable = isdropable
    def sale(self):
        print(f"{self.name} is sold")
    def discard(self):
        print(f"{self.name} is discarded")

class WearableItem(Item):
    def __init__(self, name, price, weight, isdropable, effect):
        super().__init__(name, price, weight, isdropable)
        self.effect = effect
    def wear(self):
        print(f"You wear {self.name}!")

class UsableItem(Item):
    def __init__(self, name, price, weight, isdropable, effect):
        super().__init__(name, price, weight, isdropable)
        self.effect = effect
    def use(self):
        print(f"You used {self.name}!")

i1 = WearableItem("armor", 300, 200, False, "protect your body")
i1.wear()







