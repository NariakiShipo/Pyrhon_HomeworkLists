# nine_square_grid = [0] * 9
# player_choose = list()
# computer_choose = list()
# winConnect = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
# def check_winner(order: int):
#     pass
# def check_M(order: int):
#     if 1<= order <= 2:
#         if order == 1:
#             a = 1
#         elif order == 2:
#             a = 1
#     else:
#         raise ValueError("ErrorInput")
# try :
#     M = int(input())
#     check_M(M)
#     while True:
#         i = 0
#         step = int(input())
#         if i < 5:
#             nine_square_grid[i] = step
#         else:
#             break
# except ValueError:
#     print("ErrorInput")
#     exit()
# finally:
#     print("end")
#     #check_winner(M)

# 讀取輸入（不使用 sys）
m = int(input().strip())                 # 1=Player先下, 2=Computer先下
moves = list(map(int, input().split()))  # 第二行 5 步的位置（可能少於5）

# 初始化棋盤：9 個位置，未下處標 0
board = [0] * 9

# 定義玩家標記 (Player=1, Computer=2)
PLAYER = 1
COMPUTER = 2

# 確定先後手的標記
first_marker = PLAYER if m == 1 else COMPUTER
second_marker = COMPUTER if m == 1 else PLAYER

# 依序落子（最多處理前 5 步）
for i, pos in enumerate(moves[:5]):
    marker = first_marker if i % 2 == 0 else second_marker
    idx = pos - 1
    if 0 <= idx < 9:
        board[idx] = marker

# 勝利線
WIN_LINES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # 橫
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # 直
    (0, 4, 8), (2, 4, 6)              # 斜
]

def check_win(b, marker):
    for a, b1, c in WIN_LINES:
        if b[a] == marker and b[b1] == marker and b[c] == marker:
            return True
    return False

# 判斷勝負
player_win = check_win(board, PLAYER)
computer_win = check_win(board, COMPUTER)

if player_win:
    result = "Player win"
elif computer_win:
    result = "Computer win"
else:
    result = "Undecided"

# 輸出棋盤與結果（若評測只要結果，可移除前三行）
print(f"{board[0]} {board[1]} {board[2]}")
print(f"{board[3]} {board[4]} {board[5]}")
print(f"{board[6]} {board[7]} {board[8]}")
print(result)