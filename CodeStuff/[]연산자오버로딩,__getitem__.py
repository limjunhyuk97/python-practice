# __getitem__() 함수
#  : 객체에 대해서 [] 연산이 가능하도록 만든다.
#  : cpp의 연산자 overloading과 비슷하다.

class Class:
    def __init__(self, *args):
        self.student_list = list(args)
    def total_score(self):
        total = 0
        for i in self.student_list:
            total += i
        return total
    def average_score(self):
        return self.total_score()/len(self.student_list)
    def highest_score(self):
        return max(self.student_list)
    def lowest_score(self):
        return min(self.student_list)
    def sorted_score_ao(self):
        List = sorted(self.student_list)
        return List
    def sorted_score_do(self):
        List = sorted(self.student_list, reverse=True)
        return List
    ## Class class에서 생성된 객체 내 요소에 대해서 배열같은 접근을 가능하게 한다.
    def __getitem__(self, item):
        return self.student_list[item]

class1 = Class(100, 90, 80, 40, 30, 76, 34, 55, 88)

print(class1.total_score())
print(class1.average_score())
print(class1[2])
print(class1.sorted_score_do())
print(class1.sorted_score_ao())
print(class1.highest_score())
print(class1.lowest_score())
