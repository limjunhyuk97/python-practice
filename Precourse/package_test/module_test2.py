import module_test

print(module_test.version)
module_test.printAuthor()

pay = module_test.Pay(1234, 102000, "2021-11-20")
print(pay.get_pay_info())

if __name__ == "__main__":
    print("main 으로 실행")