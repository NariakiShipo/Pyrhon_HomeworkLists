import math

a = int(input())
b = int(input())
c = int(input())

x1 = ((-b) + math.sqrt(b * b -  4 * a * c)) / (2 * a)
x2 = ((-b) - math.sqrt(b * b -  4 * a * c)) / (2 * a)

x1 = round(x1, 1)
x2 = round(x2, 1)

if x1 == x2 :
    print(x1)
else :
    print("%.1f\n%.1f" %(x1,x2))