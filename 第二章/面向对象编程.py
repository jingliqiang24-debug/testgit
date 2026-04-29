class Car:
    def __init__(self, color, brand, price):
        self.color = color
        self.brand = brand
        self.price = price
        print("car类的对象初始化完毕")
    def running(self):
        print("高速行驶")

    def total_cost(self,discont,rise):
        return self.price*discont*rise
    def __str__(self):
        return f"{self.color}{self.price}{self.brand}"
    def __eq__(self, other):
        return self.color == other.color and self.price == other.price
    def __lt__(self, other):
        return self.price < other.price
    def __gt__(self, other):
        return self.price > other.price
    def __add__(self, other):
        return self.price + other.price
    def __sub__(self, other):
        return self.price - other.price


c1 =   Car("red", "BMW", 100)
c2 = Car("red", "BMW", 100)
print(c1 == c2)
c1.running()
print(c1.color)
print(c1.brand)
print(c1.price)
print(c1)
c1.running()
a = c1.total_cost(12,100)
print(a)

