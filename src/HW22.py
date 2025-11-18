

def first_matrix(n: int):
    i = 1
    while i < n*n+1:
        if i%n == 0:
            print(i)
        else:
            print(i, end = ' ')
        i += 1
def second_matrix(n: int):
    for j in range(n, 0 , -1):
        i = n*n - j + 1
        while i//n != 0:
            print(i, end = ' ')
            i -= n
        if i > 0:
            print(i)
def third_matrix(n: int):
    i = n*n
    while i > 0:
        if i%n == 1:
            print(i)
        else:
            print(i, end = ' ')
        i -= 1
def fourth_matrix(n: int):
    i = n
    for j in range(n):
        num = - j
        repeat = n
        while repeat > 0:
            num += i
            print(num, end = ' ')
            repeat -= 1
        print()
        
def check_rotate(text: str, n: int):
    l_num = 0
    r_num = 0
    for t in text:
        if t == "L":
            l_num += 1
        elif t == "R":
            r_num += 1
        else:
            raise ValueError("Invalid character in input string")
    result = (r_num - l_num)% 4
    if result < 0: result += 4
        
    if result == 3:
        fourth_matrix(n)
    elif result == 2:
        third_matrix(n)
    elif result == 1:
        second_matrix(n)
    else:# no rotation
        first_matrix(n)
def main():
    n = int(input())
    text = input()
    check_rotate(text, n)
main()