# user = float(input("请输入你的账号"))
# password = float(input("输入你密码"))
#
# if user == 123 and password == 456:
#     print("账号密码正确")
# elif user != 123 and password != 456:
#     print("账号和密码都错误")
# elif user != 123 and password == 456:
#     print("站好错误")
# else:
#     print("密码错误")
#
#
# year = int(input("请输入当前的年份"))
# if (year % 100 != 0 and year %4==0) or (year % 400 == 0):
#     print(f"{year}is 闰年")
# else:
#     print("平年")

a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))

if a+b>c and a+c>b and b+c>a:
    if a == b and b == c:
      print("等边三角形")
    elif a == b or b == c or a == c:
      print("等腰三角形")
    else:
        print("三角形")
else:
    print("不是三角形")

