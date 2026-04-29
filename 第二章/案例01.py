# while True:
#     admin = input("请输入你的账号")
#     password = input("亲输入你的密码")
#
#     if admin == "admin" and password == "123":
#         print("登陆成功")
#         break
#     elif admin != "admin" and password != "123":
#         print("账号密码错误请从新输入")
#         continue
import random

num = range(0, 100)
print(type(num))
num = random.randint(0, 100)
while True:
    try:
        number = int(input("请输入一个数字"))

        if number == num:
            print("猜对了")
        elif number > num:
            print("大了")
        elif number < num:
            print("小了")
    except ValueError:
        print("不能输入回车")