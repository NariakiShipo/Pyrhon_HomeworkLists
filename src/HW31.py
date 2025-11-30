brackets_layer = {"(": 0, "[": 1, "{": 2}
pairs = {"{": "}", "(": ")", "[": "]"}
close_to_open = {"}": "{", ")": "(", "]": "["}

def check_brackets(text):
    """
    check if brackets in text are balanced and hierarchical
    return: (is_balanced, is_hierarchy_ok)
    """
    stack = []  # stack to track opening brackets
    hierarchy_ok = True  # 記錄層級是否正確
    
    for char in text:
        if char in pairs:  # left bracket
            stack.append(char)
        elif char in close_to_open:  # right bracket
            if not stack:  # no matching left bracket
                return False, True  # not balanced
            
            left = stack.pop()
            # check matching
            if close_to_open[char] != left:
                return False, True  # not balanced
            
            # check hierarchy: 當前括號層級不能小於堆疊中任何括號的層級
            for remaining in stack:
                if brackets_layer[remaining] < brackets_layer[left]:
                    hierarchy_ok = False  # 層級錯誤，但繼續檢查配對
    
    # check if any left brackets remain
    if stack:
        return False, True  # not balanced
    
    return True, hierarchy_ok  # 回傳配對結果和層級結果
def extract_parentheses(text):

    expression = []
    i = 0
    while i < len(text):
        count = 1
        j = i + 1
        if text[i] == "(":
            while j < len(text) and count > 0:
                if text[j] == ")":
                    count +=1
                elif text[j] == "(":
                    count -=1
                j+=1
            content =  text[i+1: j-1]
            expression.append(content)
            i = j
        else:
            i += 1
    return expression
def process_arithmetic(text):
    """process arithmetic expression by removing brackets"""
    stack = [] 
    # To remove the parentheses that make it simplify.
    for char in text:
        if char == ')':  # 遇到右小括號，開始結算
            temp_content = []
            
            # 1. 不斷從堆疊拿出東西，直到遇到左括號 '('
            while stack and stack[-1] != '(':
                temp_content.append(stack.pop())
            
            # 把 '(' 丟掉
            if stack:
                stack.pop()
            
            # 因為是用 stack pop 出來的，順序是反的 (例如 B, +, A)，要反轉回來
            temp_content.reverse() 
            
            # 2. 處理這層括號內的運算
            # 將 list 暫時組合成字串方便檢查運算符號
            # 注意：這裡的 temp_str 可能已經包含上一層算好的結果
            content_str = "".join(temp_content)
            
            result = ""
            if '*' in content_str:
                # 處理乘法 (題目保證只有兩字串運算，簡單 split 即可)
                parts = content_str.split('*')
                # parts[0] 是字串, parts[1] 是數字
                # 注意：如果題目數字可能多位數，要小心處理，但這題通常數字是個位數
                if parts[1].isdigit():
                    string_part = parts[0]
                    number_part = int(parts[1])
                else:
                    string_part = parts[1]
                    number_part = int(parts[0])
                result = string_part * number_part
                
            elif '+' in content_str:
                # 處理加法
                parts = content_str.split('+')
                result = parts[0] + parts[1]
                
            else:
                # 沒有運算符號 (例如 ((A)) 的外層，或是單純 (abc))
                result = content_str
            
            # 3. 【關鍵】將算好的結果放回堆疊，給外層用
            stack.append(result)

        elif char == ']' or char == '}': # 遇到中/大括號
            # 中大括號只有「去括號」功能，不做運算
            temp_content = []
            
            # 決定對應的左括號是誰
            target = '[' if char == ']' else '{'
            
            while stack and stack[-1] != target:
                temp_content.append(stack.pop())
            
            if stack:
                stack.pop() # 丟掉 '[' 或 '{'
            
            temp_content.reverse()
            # 直接接起來放回去
            stack.append("".join(temp_content))
            
        else:
            # 其他字元 (字母、數字、左括號)，直接放入
            stack.append(char)
            
    # 最後堆疊剩下的就是結果，把它接起來
    return "".join(stack)
def main(): 
    n = int(input())
    for _ in range(n):
        text = input()
        is_balanced, is_hierarchy_ok = check_brackets(text)
        
        if not is_balanced:
            print("Unbalanced")
        elif not is_hierarchy_ok:
            print("Hierarchy Violation")
        else:
            # Balanced and hierarchical then process arithmetic
            ans = process_arithmetic(text)
            print(ans)
if __name__ == "__main__":
    main()