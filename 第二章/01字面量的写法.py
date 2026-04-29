# # 字面量的写法
# print(100)
# print(3.14)
# print(True)
# print(False)
# print("python")
# print(None)
from ipaddress import ip_interface

num = 1114.1
print(num)

num = num+1
print(num)
num = "OK"
print(num)

base = 20.7
incr = 50
base ,incr = 20,12
print("未来第一个月的播放总量:",base + incr)
print("未来第二个月的播放总量:",base + 2*incr)

a = 1
b = 2
a,b = b,a
print(a,b)
print(type(a),type(b))

print(type(True))
print(type(False))

print(isinstance(a,int))
c = isinstance(a,float)
print(c)