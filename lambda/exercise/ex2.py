class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)


p1 = Point(2, 3)
p2 = Point(-1, 2)

p3 = p1+p2
print(p3.x)
print(p3.y)

# print(p1+p2)
# a=(p1.x+p2.x)
# b=(p1.y+p2.y)
# print(a+b)