def are(l,w):
    return l*w*0.5

ares = are(2,5)
print(ares)


def yuancount(zi):
    s = "aeiouAEIOU"
    i = 0
    for x in zi:
        if x in s:
            i += 1
    return i
s = input("请输入一段字符串")
print(yuancount(s))

def jisuan(list):
    max_1 = max(list)
    min_1 = min(list)
    avg_1 = sum(list)   / len(list)
    return max_1, min_1, avg_1

s_list = [123,234,346,13,45634,14]
print(jisuan(s_list))

