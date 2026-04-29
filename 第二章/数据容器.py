# s = [12,32,33,13,13,43,"年后",True]

# print(s[3])
# s[3] = 4
# print(s[3])
#
# del s[3]
# print(s[3])
#
# for i in s:
#     print(i,end=" ")
# import math
# b = ["A","C","E","F","Y","G"]
#
# b.append("s")
# C = b.copy()
# print(C)
# print(b.count("A"))
# print(b[0::1])
#
# i = 0
# list = []
# while i <10:
#     number = int(input("请输入10个数字"))
#     i += 1
#     list.append(number)
# print(list)
# list.sort()
# print(list[0])
# print(list[-1])


list = []
for i in range(1,21):
    list.append(i**2)

print(list)

list = [i**3 for i in range(1,23)]
print(list)


