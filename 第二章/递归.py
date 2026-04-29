def jc(i):
    if i == 1:
        return 1
    else:
        return i * jc(i - 1)

a = jc(10)
print(a)