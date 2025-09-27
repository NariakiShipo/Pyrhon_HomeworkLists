import math

a = int(input())
b = int(input())
c = int(input())

delta = (b * b) - (4 * a * c)

if delta >= 0:
    x1 = ((-b) + math.sqrt(delta)) / (2 * a)
    x2 = ((-b) - math.sqrt(delta)) / (2 * a)
    
    x1 = round(x1, 1)
    x2 = round(x2, 1)
    if x1 == x2:
        print(f"{x1:.1f}")
    else:
        
        roots = sorted([x1, x2], reverse=True)
        print(f"{x1:.1f}")
        print(f"{x2:.1f}")
else:
   
    A = -b / (2 * a)
    B = math.sqrt(-delta) / (2 * a)
   
    A = round(A, 1)
    B = round(B, 1)
    if A == 0 or A == -0.0:
        A = 0.0
    B = abs(B)
    print(f"{A:.1f}+{B:.1f}i")
    print(f"{A:.1f}-{B:.1f}i")


        