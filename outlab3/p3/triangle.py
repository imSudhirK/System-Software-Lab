import math

x1, y1 = map(int, input("Enter the first coordinate: ").split())
x2, y2 = map(int, input("Enter the first coordinate: ").split())
x3, y3 = map(int, input("Enter the first coordinate: ").split())
x, y = map(int, input("Enter reference point: ").split())

def sideLength(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def triangleArea(x1, y1, x2, y2, x3, y3):
    a = sideLength(x1, y1, x2, y2)
    b = sideLength(x2, y2, x3, y3)
    c = sideLength(x3, y3, x1, y1)
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

def isInsideTriangle(x1, y1, x2, y2, x3, y3, x, y):
    e = triangleArea(x1, y1, x2, y2, x, y)
    f = triangleArea(x2, y2, x3, y3, x, y)
    g = triangleArea(x3, y3, x1, y1, x, y)
    h = triangleArea(x1, y1, x2, y2, x3, y3)
    if float(e + f + g) == h:
        return "Given point is inside"
    else: return "Given point is outside"

print(isInsideTriangle(x1, y1, x2, y2, x3, y3, x, y))