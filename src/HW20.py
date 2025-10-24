spacialWords = "~!@#$%^&<>_+="
number = '1234'
def isspacialWord(c: str) -> bool:
    return c in spacialWords
def calPasswordStrength(password: str) -> float:
    strength = 0
    for c in password:
        if c.islower():
            strength += 1.0
        elif c.isupper():
            strength += 3.0
        elif c.isdigit():
            strength += 2.0
        elif isspacialWord(c):
            strength += 4.5
    if number in password:
        strength -= 10.0
    if len(password) >= 8:
        for _ in range(len(password) - 8):
            strength += 1.0
        isBeside = False
        isPreviousDigit = False
        digits = 0
        for c in password:
            if c.isdigit():
                if isPreviousDigit:
                    isBeside = True
                    digits = 0
                    break
                isPreviousDigit = True
                digits += 1.0
            else:
                isPreviousDigit = False
        if digits >= 5:
            strength += 10.0
    return strength

def main():
    num = int(input())
    passwords = []
    for _ in range(num):
        password = input()
        strength = calPasswordStrength(password)
        passwords.append((password, strength))
    min = passwords[0][1]
    max = passwords[0][1]
    maxNum = 0
    minNum = 0
    for i in range(len(passwords)):
        if max < passwords[i][1]:
            max = passwords[i][1]
            maxNum = i
        if min > passwords[i][1]:
            min = passwords[i][1]
            minNum = i
    print(f'{passwords[maxNum][0]} {passwords[maxNum][1]}\n{passwords[minNum][0]} {passwords[minNum][1]}')

main()


# a1a1a1a1a11234
# a 1 a 1 a 1 a 1 1 a
