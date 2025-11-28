def CheckIfEffective(data):
    return

def textGenerator(s):
    if len(s)==1:
        return [s]
    result = []
    for i in range(len(s)):
        result += [s[i]+ sub for sub in textGenerator(s[:i]+s[i+1:])]
    # 使用list 產生器得到所有排列結果
    return result
def main():  
    a= "abc"
    n= 3
    text =""
    for _ in range(2):
        text = ''

    # exist = input()
    # if 5 < len(exist) or len(exist) < 1: exit()
    # n = int(input())
    # if 8 < n or n < 1: exit()
    # m = int(input())
    # condition = int(input())
    # if condition > m or m > n: exit()
if __name__ == "__main__":
    main()