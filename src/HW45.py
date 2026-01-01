def read_board():
    board = []
    for _ in range(4):
        board.append(list(map(int, input().split())))
    return board

def get_block_idx(i, j):
    return (i // 2) * 2 + (j // 2)

def is_valid(board, r, c, val):
    # 檢查 row
    if val in board[r]:
        return False
    # 檢查 col
    for i in range(4):
        if board[i][c] == val:
            return False
    # 檢查 block
    br = (r // 2) * 2
    bc = (c // 2) * 2
    for i in range(br, br+2):
        for j in range(bc, bc+2):
            if board[i][j] == val:
                return False
    return True

def solve(board):
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                for val in range(1, 5):
                    if is_valid(board, i, j, val):
                        board[i][j] = val
                        if solve(board):
                            return True
                        board[i][j] = 0
                return False
    return True

def main():
    board = read_board()
    solve(board)
    for row in board:
        print(' '.join(map(str, row)))

if __name__ == '__main__':
    main()
