import math
x1 = int(input("enter the first point of first vertex: "))
y1 = int(input("enter the second point of first vertex: "))
x2 = int(input("enter the first point of second vertex: "))
y2 = int(input("enter the second point of second vertex: "))
distance = (math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))
print("%.2f" % distance)
