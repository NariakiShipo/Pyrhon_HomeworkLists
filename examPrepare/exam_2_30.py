def parse_initialization(line:str, variables):
    left_sides, right_sides = line.split('=')
    var_names = [v.strip() for v in left_sides.split(",")]
    var_values = [v.strip()[1:-1] for v in right_sides.split(",")]
    for var_name, var_value in zip(var_names, var_values):
        variables[var_name] = var_value
def custom_slice(s, start =None, end = None , step =None):
    length = len(s)

    if step is None:
        step = 1
    if step == 0:
        raise ValueError("step cannot be 0")
    
    if step > 0:
        if start is None:
            start = 0
        elif start < 0 and (start * -1) > length:
            start = 0
        elif start < 0:
            start = max(0, length + start)
        elif start > length:
            start = length 
        
        if end is None:
            end = length
        elif end < 0 and (end * -1) > length:
            end = 0
        elif end < 0:
            end = max(0, length + end)
        elif end > length:
            end = length
    
    else:
        if start is None:
            start = length -1
        elif start < 0 and (start * -1) > length:
            start = 0
        elif start < 0:
            start = length + start
        
        if end is None:
            end = -1
        elif end < 0 and (end * -1) > length:
            end = 0
        elif end < 0:
            end = length + end
    result = ""
    if step > 0:
        for i in range(start, end ,step):
            result +=s[i]
    else:
        for i in range(start, end ,step):
            if i >= 0 and i < length:
                result +=s[i]
    return result
def process_print(variables, text:str):
    content = text[6:-1]
    if '[' in content:
        params = content.split("[")
        var_name = params[0]
        slice_param = params[1].rstrip("]")
        
        params = slice_param.split(':')
        start = int(params[0]) if params[0] else None
        end = int(params[1]) if len(params) > 1 and params[1] else None
        step = int(params[2]) if len(params) > 2 and params[2] else None
        print(custom_slice(variables[var_name], start, end, step))
    else:
        var_name = content
        print(variables[var_name])
def process_plus_val(variables, text:str):
    left_sides,right_sides = text.split("=")
    left_var = left_sides.strip()
    right_vars = right_sides.strip()

    parts = right_vars.split("+")
    var1 = parts[0].strip()
    var2 = parts[1].strip()

    result = variables[var1] + variables[var2]
    variables[left_var] = result
def process_assignment(variables, text:str):
    left_sides, right_sides = text.split('=')
    var_names = [v.strip() for v in left_sides.split(",")]
    right_sides = right_sides.strip()
    
    # 檢查右邊是否是字符串（用引號包圍）或變數名
    if right_sides.startswith("'") or right_sides.startswith('"'):
        # 是字符串字面值
        var_values = [v.strip()[1:-1] for v in right_sides.split(",")]
        for var_name, var_value in zip(var_names, var_values):
            variables[var_name] = var_value
    else:
        # 是變數名，直接查表
        var_values = [v.strip() for v in right_sides.split(",")]
        for var_name, var_value in zip(var_names, var_values):
            variables[var_name] = variables[var_value]
def main():
    variables = {}
    intial_count, output_count = map(int, input().split())
    
    for _ in range(intial_count):
        parse_initialization(input().strip(), variables)
    for _ in range(output_count):
        text = input().strip()
        if "print" in text:
            process_print(variables, text)
        elif '=' in text:
            if "+" in text:
                process_plus_val(variables, text)
            else:
                process_assignment(variables, text)

if __name__ == "__main__":
    main()