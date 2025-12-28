def is_horizontal(board, marked):
    """計算完成的橫線數量"""
    count = 0
    for row in board:
        if all(num in marked for num in row):
            count += 1
    return count

def is_vertical(board, marked):
    """計算完成的直線（列）數量"""
    count = 0
    n = len(board)
    for col in range(n):
        if all(board[row][col] in marked for row in range(n)):
            count += 1
    return count

def is_diagonal(board, marked):
    """計算完成的對角線數量（左上-右下和右上-左下）"""
    count = 0
    n = len(board)
    
    # 左上到右下對角線
    if all(board[i][i] in marked for i in range(n)):
        count += 1
    
    # 右上到左下對角線
    if all(board[i][n-1-i] in marked for i in range(n)):
        count += 1
    
    return count

def is_x_line(board, marked):
    """
    計算X型線（兩條對角線都完成時額外計數1次）
    """
    n = len(board)
    main_diag = all(board[i][i] in marked for i in range(n))
    anti_diag = all(board[i][n-1-i] in marked for i in range(n))
    
    if main_diag and anti_diag:
        return 1
    return 0

def is_l_line(board, marked):
    """
    計算L型線（第一行加上最後一列完成時計數1次）
    """
    n = len(board)
    first_row = [board[i][0] for i in range(n)]
    last_col = [board[n-1][i] for i in range(n)]
    all_marked = set(first_row + last_col)
    
    if all_marked.issubset(marked):
        return 1
    return 0

def count_bingo_lines(board, marked):
    """計算總賓果線數"""
    return (is_horizontal(board, marked) + 
            is_vertical(board, marked) + 
            is_diagonal(board, marked) + 
            is_x_line(board, marked) +
            is_l_line(board, marked))

def print_winner(a_lines, b_lines):
    """根據賓果線數輸出贏家"""
    if a_lines > b_lines:
        print("A Win")
    elif b_lines > a_lines:
        print("B Win")
    else:
        print("Tie")

def main():
    n = int(input())
    m = int(input())
    player_a_flat = list(map(int, input().split()))
    player_b_flat = list(map(int, input().split()))
    match_num = list(map(int, input().split()))
    
    # 將一維陣列轉換為二維矩陣
    player_a = [player_a_flat[i*n:(i+1)*n] for i in range(n)]
    player_b = [player_b_flat[i*n:(i+1)*n] for i in range(n)]
    
    # 將圈選的號碼轉換為集合以提高查詢效率
    marked = set(match_num)
    
    # 計算兩位玩家的賓果線數
    a_lines = count_bingo_lines(player_a, marked)
    b_lines = count_bingo_lines(player_b, marked)
    
    # 輸出結果
    print_winner(a_lines, b_lines)

if __name__ == "__main__":
    main()
