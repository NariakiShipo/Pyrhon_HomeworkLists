def String_Parser(text:list) -> float:
    text[0] = float(text[0])
    for i in range(1,len(text),2):
        i+=1

    ans = 1.0
    return ans

arithmetic = input()
arithmetic = str.split(arithmetic," ")
print(arithmetic)
# ans = String_Parser(arithmetic)
# # ans = eval(arithmetic)
# print(f"{ans:.2f}")