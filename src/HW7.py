a = int(input())
b = int(input())
c = int(input())

max_num = max(a,b,c)
sides = [a, b, c]
sides.remove(max_num)

if a + b > c and a + c > b and b + c > a:
    if a == b and a == c and b == c:
        print("Equilateral Triangle")
        
    if a == b or a == c or b == c:
        print("Isosceles Triangle")
    
    if max_num ** 2 > sides[0] ** 2 + sides[1] ** 2:
        print("Obtuse Triangle")
    
    if max_num ** 2 < sides[0] ** 2 + sides[1] ** 2:
        print("Acute Triangle")
    
    if max_num ** 2 == sides[0] ** 2 + sides[1] ** 2:
        print("Right Triangle")
else :
    print("Not Triangle")
    