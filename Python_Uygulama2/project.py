import math

def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

x1 = float(input("1. noktanın x koordinatını girin (x1): "))
y1 = float(input("1. noktanın y koordinatını girin (y1): "))
x2 = float(input("2. noktanın x koordinatını girin (x2): "))
y2 = float(input("2. noktanın y koordinatını girin (y2): "))

point1 = (x1, y1)
point2 = (x2, y2)

distance = euclideanDistance(point1, point2)

print("İki nokta arasındaki Öklid Mesafesi:", distance)
