#Need input Decimal not Binary
#Count return the feedback circuit counts
def Count(m):
    if m<= 1:
        return 0
    elif m % 2 == 0:
        return 1+Count(m / 2)
    elif m % 2 == 1:
        return 2+Count((m + 1) / 2) + Count((m - 1)/2) 

# BinaryToDecimal return the binary number from input
def BinaryToDecimal(m):
    return int(m, 2)

#DecimalToTernary return the ternary number from input
def DecimalToTernary(m):
    result = ""
    quotient = m
    remain = 0
    while quotient != 0:
        remain = quotient % 3
        quotient = quotient // 3
        result = str(remain) + result
    for _ in range(6-len(result)):
        result = "0" + result
    return result
def main():
    m = ""
    result = []
    while True:
        m = input()
        if m == "-1": break
        decimal = BinaryToDecimal(m)
        ans = Count(decimal)
        r = DecimalToTernary(ans)
        result.append(r)
    for re in result:
        print(re)
    
#Check if the main is in this file
if __name__ == "__main__":
    main()