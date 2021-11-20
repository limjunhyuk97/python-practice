# table 형태의 data 를 저장하기 위해서 comma(,) seperated file을 사용하는데, 이게 csv 파일이다.

import csv

data = [
    ["이름", "반", "번호"],
    ["임준혁", "1반", 223456]
]

file = open("../by-product/student.csv", "w", encoding="utf-8-sig")
writer = csv.writer(file)
for d in data:
    writer.writerow(d)
file.close()

file = open("../by-product/student.csv", "r", encoding="utf-8-sig")
reader = csv.reader(file)
for d in reader:
    print(d)
file.close()

print("================= 실습")

import re
p = re.compile('[0-9]')

data = [
    ["종목", "매입가", "수량", "목표가"],
    ["삼성전자", 85000, 10, 90000],
    ["NAVER", 380000, 5, 400000]
]

file = open("../by-product/stock.csv", "w")
writer = csv.writer(file)
for d in data :
    writer.writerow(d)
file.close()

file = open("../by-product/stock.csv", "r")
reader = csv.reader(file)
for d in reader:
    if p.match(d[2]) == None : continue
    print(d[0] + f" {(int(d[3]) - int(d[1]))*int(d[2])} {(int(d[3])/int(d[1]) - 1) * 100}%")
file.close()

file = open("../by-product/stock.csv", "r")
reader = list(csv.reader(file))
for d in reader[1:]:
    print(d[0] + f" {(int(d[3]) - int(d[1]))*int(d[2])} {(int(d[3])/int(d[1]) - 1) * 100}%")
file.close()