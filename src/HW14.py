# 初始設定
x, y = 0.0, 0.0
angle = 0.0
pattern = "no_pattern"
color = "black"

def reset():
    global x, y, angle, pattern, color
    x, y = 0.0, 0.0
    angle = 0.0
    pattern = "no_pattern"
    color = "black"

def mv(dx, dy):
    global x, y
    x += dx
    y += dy

def rotate_angle(r):
    global angle
    angle += r
    # 確保角度在 [0, 360) 範圍內
    angle = angle % 360

def set_pattern_func(p):
    global pattern
    pattern = p

def set_color_func(c):
    global color
    color = c

def stamp():
    print(f'Stamping... [position: ({x:.2f}, {y:.2f}), rotation: {angle:.2f} degrees, pattern: {pattern}, color: {color}]')

# 處理指令
stamped = False
for _ in range(6):
    line = input().split()
    command = line[0]
    
    if command == "reset":
        reset()
    elif command == "mv":
        dx, dy = float(line[1]), float(line[2])
        mv(dx, dy)
    elif command == "rotate":
        r = float(line[1])
        rotate_angle(r)
    elif command == "set_pattern":
        p = line[1]
        set_pattern_func(p)
    elif command == "set_color":
        c = line[1]
        set_color_func(c)
    elif command == "stamp":
        stamp()
        stamped = True

# 如果沒有執行過 stamp，輸出取消訊息
if not stamped:
    print("Stamping canceled")
