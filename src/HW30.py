def parse_assignment(line, variables):
    """解析賦值語句，支援單個或多個變數賦值"""
    # 移除空白
    line = line.strip()
    
    # 分割等號左右兩邊
    parts = line.split('=')
    left = parts[0].strip()
    right = '='.join(parts[1:]).strip()
    
    # 解析左邊的變數名稱
    var_names = [v.strip() for v in left.split(',')]
    
    # 解析右邊的值
    values = []
    current = ''
    in_quote = False
    quote_char = None
    
    for char in right:
        if char in ('"', "'") and not in_quote:
            in_quote = True
            quote_char = char
        elif char == quote_char and in_quote:
            in_quote = False
            values.append(current)
            current = ''
            quote_char = None
        elif char == ',' and not in_quote:
            continue
        elif in_quote:
            current += char
    
    # 如果右邊不是字串字面值，可能是變數或運算式
    if not values:
        # 處理變數賦值或運算
        right = right.strip()
        if '+' in right:
            # 處理字串串接
            parts = [p.strip() for p in right.split('+')]
            result = ''
            for part in parts:
                if part in variables:
                    result += variables[part]
                elif part.startswith(("'", '"')) and part.endswith(("'", '"')):
                    result += part[1:-1]
            values = [result]
        elif right in variables:
            # 變數賦值
            values = [variables[right]]
        elif right.startswith(("'", '"')) and right.endswith(("'", '"')):
            # 單個字串字面值
            values = [right[1:-1]]
    
    # 將變數名稱和值配對
    for i, var_name in enumerate(var_names):
        if i < len(values):
            variables[var_name] = values[i]


def parse_slice(slice_str):
    """解析切片參數 [start:end:step] 或 [index]"""
    slice_str = slice_str.strip()
    
    if ':' not in slice_str:
        # 單個索引
        return int(slice_str) if slice_str else None, None, None, True
    
    parts = slice_str.split(':')
    start = int(parts[0]) if parts[0] else None
    end = int(parts[1]) if len(parts) > 1 and parts[1] else None
    step = int(parts[2]) if len(parts) > 2 and parts[2] else None
    
    return start, end, step, False


def process_print(line, variables):
    """處理print語句"""
    # 提取print()中的內容
    start = line.find('(')
    end = line.rfind(')')
    content = line[start+1:end].strip()
    
    # 檢查是否有切片
    if '[' in content:
        var_name = content[:content.find('[')].strip()
        slice_part = content[content.find('[')+1:content.find(']')]
        
        if var_name in variables:
            value = variables[var_name]
            start, end, step, is_index = parse_slice(slice_part)
            
            if is_index:
                # 單個索引
                print(value[start])
            else:
                # 切片
                print(value[start:end:step])
    else:
        # 沒有切片，直接輸出變數
        var_name = content.strip()
        if var_name in variables:
            print(variables[var_name])


def main():
    length = input().split()
    m = int(length[0])
    n = int(length[1])
    
    variables = {}
    
    # 讀取並處理變數初始化
    for i in range(m):
        line = input()
        parse_assignment(line, variables)
    
    # 處理運算與輸出指令
    for i in range(n):
        line = input().strip()
        if line.startswith('print'):
            process_print(line, variables)
        elif '=' in line:
            parse_assignment(line, variables)


if __name__ == "__main__":
    main()
