# 讀取所有輸入球數
balls = []
while True:
    try:
        ball = int(input())
        balls.append(ball)
    except:
        break

# 計算保齡球分數
def calculate_bowling_score(balls):
    total_score = 0
    ball_index = 0
    
    for frame in range(3):
        if frame < 2:  # 第1、2局
            if balls[ball_index] == 10:  # Strike
                total_score += 10 + balls[ball_index + 1] + balls[ball_index + 2]
                ball_index += 1
            elif balls[ball_index] + balls[ball_index + 1] == 10:  # Spare
                total_score += 10 + balls[ball_index + 2]
                ball_index += 2
            else:  # 一般情況
                total_score += balls[ball_index] + balls[ball_index + 1]
                ball_index += 2
        else:  # 第3局
            if balls[ball_index] == 10:  # 第一球Strike
                total_score += balls[ball_index] + balls[ball_index + 1] + balls[ball_index + 2]
            elif balls[ball_index] + balls[ball_index + 1] == 10:  # Spare
                total_score += balls[ball_index] + balls[ball_index + 1] + balls[ball_index + 2]
            else:  # 一般情況
                total_score += balls[ball_index] + balls[ball_index + 1]
    
    return total_score

print(calculate_bowling_score(balls))