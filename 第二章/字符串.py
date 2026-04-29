s = "asjd_kfjljafc,fawe"
t = s.upper()
print(t)
a = s.split("_")

print(a)

pome = input("请输入一个故事")

pome_reverse = pome[::-1]
if pome == pome_reverse:
    print("是回文")
else:
    print("不是回文")

# result = []
#
# # 循环输入10个字符串
# i = 0
# while i < 10:
#     s = input(f"请输入第{i+1}个字符串：")
#     # 反转并转大写
#     s_new = s[::-1].upper()
#     result.append(s_new)
#     i += 1
#
# # 遍历输出
# print("\n处理后的结果：")
# for item in result:
#     print(item)
res = []
for i in  range(10):
    s = input("请输入你的字")
    new  = s[::-1].upper()
    res.append(new)

for n in res:
    print(n)
