

def a():
    print("a被调用了")
    b()
    print("a----")


def b():
    print("b----")
    c()
    print("b----")


def c():
    print("c被调用了")

a()
print("完毕")