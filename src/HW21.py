def printRightTriangle(n):
    for i in range(1, n+1):
        for j in range(1,i):
            print(f'{j}', end='')
        for j in range(i, 0 ,-1):
            print(f'{j}', end='')
        print()
    return
def printEquilateralTriangle(n):
    mark = '_'
    for i in range(1, n+1):
        print(f'{mark*(n-i)}', end='')
        for j in range(1,i):
            print(f'{j}', end='')
        for j in range(i, 0 ,-1):
            print(f'{j}', end='')
        print(f'{mark*(n-i)}', end='')
        print()
    return
def printInvertedTriangle(n):
    mark = '_'
    for i in range(0, n):
        print(f'{mark*(i)}', end='')
        for j in range(1,n+1-i):
            print(f'{j}', end='')
        for j in range(n-i-1, 0 ,-1):
            print(f'{j}', end='')
        print(f'{mark*(i)}', end='')
        print()
    return

def main():
    n = int(input())
    num = int(input())
    if 3 <= num <= 50:
        if n == 1:
            printRightTriangle(num)
        elif n == 2:
            printEquilateralTriangle(num)
        elif n == 3:
            printInvertedTriangle(num)
    else: 
        print("Row Error")
main()