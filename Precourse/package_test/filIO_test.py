file = open("../by-product/data.txt", "w", encoding="UTF-8")
file.write("왕왕 빨리 강의 다듣고 과제하자 왕!\n")
file.close()

file = open("../by-product/data.txt", "a")
file.write("강의는 언제 다듣냐!!~")
file.close()

file = open("../by-product/data.txt", "r")
while True:
    data = file.readline()
    print(data, end="")
    if data == "":
        break
file.close()