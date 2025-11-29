exist_str = input().strip()
n = int(input().strip())
m = int(input().strip())
condition = int(input().strip())
target_c = input().strip()

# 用全域變數記錄有效字串數量
count = 0

#check the sub string is vaild
def is_vaild(s) -> bool:
    for i in range(len(s) - m + 1):
        sub_string = s[i: i + m]
        count_c = sub_string.count(target_c)
        if count_c < condition:
            return False
    return True

def generate_strings(current_s=""):
    global count
    
    if len(current_s) == n:
        if is_vaild(current_s):
            count += 1
        return
    
    for char in exist_str:
        generate_strings(current_s + char)

generate_strings()
print(count)
