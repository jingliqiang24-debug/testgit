# name = input("请输入你的名字")
# age = input("请输入你的年龄")
# print(f"你的姓名是{name},年龄是{age}")
#
# total = 1000
# price = int(input("请输入你要取的金额"))
# mas = int(input("请输入你的名字"))
# print(f"你剩余的存款是{total-price}")

a,b,c = input("请输入三个整数").split(",")
a = int(a)
b = int(b)
c = int(c)
total = a+b+c
avg = total/3
print(avg)

top = float(input("输入梯形的上地:"))
bottom = float(input("输入梯形的下地:"))
height = float(input("其输入梯形的高"))
area = (top + bottom)*height/2
print(area)

import math

r = float(input("请输入圆的半径"))
perimeter = 2*math.pi*r
area = math.pi*r*r
print(perimeter)
print(area)