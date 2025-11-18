
def AscendingOrder(i):
    for j in range(i , 1, -1):
        print(j, end='')
def isOdd(m) -> bool:
    if m % 2 == 0:
        return True
    else:
        return False
    
def goldFish(n , m):
    isRight = isOdd(m)
    middle = 0
    if isOdd(n):
        middle = (2*n+1)//2
    else:
        middle = (2*n+1)//2 
    if isRight:
        j = 1
        for i in range(1 , middle + 1):
            print(f'{"*" * i}{"_" *(middle - i) *2}{"*" * j}{"_" *(middle - i)}')
            j += 2
        j -= 2
        for i in range(middle-1, 0 , -1):
            j -= 2
            print(f'{"*" * i}{"_" *(middle - i) *2}{"*" * j}{"_" *(middle - i)}')
            
    else:
        j = 1
        for i in range(1 , middle + 1):
            print(f'{"_" *(middle - i)}{"*" * j}{"_" *(middle - i) *2}{"*" * i} ')
            j += 2
        j -= 2
        for i in range(middle-1, 0 , -1):
            j -= 2
            print(f'{"_" *(middle - i)}{"*" * j}{"_" *(middle - i) *2}{"*" * i}')
def pyramid(n , m):
    isReverse = isOdd(m)
    if not isReverse:
        for i in range(1 , n + 1):
            print(f'{"_" * (n - i)}',end='')
            for j in range(i , 1, -1):
                print(j, end='')
            for j in range(1 , i+1):
                print(j, end='')
            print(f'{"_" * (n - i)}')
    else:
        for i in range(n , 0 , -1):
            print(f'{"_" * (n - i)}',end='')
            for j in range(i , 1, -1):
                print(j, end='')
            for j in range(1 , i+1):
                print(j, end='')
            print(f'{"_" * (n - i)}')

def main():
    n = int(input())
    m = int(input())
    c = int(input())

    if c == 1: 
        goldFish(n , m)
    elif c == 2:
        pyramid(n , m)

if __name__ == "__main__":
    main()