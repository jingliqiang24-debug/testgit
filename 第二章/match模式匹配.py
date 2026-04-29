# day = int(input("请输入星期"))
# match day:
#     case 1:
#         print("星期一")
#     case 2:
#         print("星期二")
#     case 3:
#         print("星期三")
#     case _:
#         print("输入超出范围")
# num1 = float(input("请输入你的数字"))
# num2 = float(input("请输入你的数字"))
# a = input("请输入符号")
#
# match a:
#     case "+":
#         print(f"{num1} + {num2} = {num1 + num2}")
#     case "-":
#         print(f"{num1} - {num2} = {num1 - num2}")
#     case _:
# #         print("baibai")
# i = 0
# total = 0
# while i <=100 :
#     total += i
#     i += 2
# print(total)
from shutil import unregister_archive_format
#
# total =0
#
# str = "helloworld"
# for i in str:
#     print(i)

# for i in range(2,101,2):
#     total += i
# print(total)

for i in range(1,10):
    for j in range(1,10):
        if i>=j:
         print(f"{i}*{j}={i*j}",end='  ')
    print(" ")

