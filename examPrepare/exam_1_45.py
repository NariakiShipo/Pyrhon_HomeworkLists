def check_block(lattice, column_idx, row_idx):
    check_set = {1,2,3,4}
    end_col = 0
    end_row = 0
    if(column_idx < 2): end_col = 2
    else: end_col = 4
    if(row_idx < 2): end_row = 2
    else: end_row = 4
    value = [lattice[i][j] for i in range(end_row - 2,end_row) for j in range(end_col -2, end_col)]
    value_set ={v for v in value if v in check_set}
    if(len(value_set) == len(check_set)):
        return set()
    else:
        return check_set - value_set

def check_column(lattice, index):
    #[0][i]~[3][i]
    check_set = {1,2,3,4}
    value = [lattice[i][index] for i in range(len(lattice))]
    value_set ={v for v in value if v in check_set}
    if(len(value_set) == len(check_set)):
        return set()
    else:
        return check_set - value_set


def check_row(lattice, index):
    #[i][0]~[i][3]
    check_set = {1,2,3,4}
    value = [lattice[index][i] for i in range(len(lattice))]
    value_set ={v for v in value if v in check_set}
    if(len(value_set) == len(check_set)):
        return set()
    else:
        return check_set - value_set
#判斷是否修復完成
def is_solve(lattice):
    for i in range(4):
        for j in range(4):
            if lattice[i][j] == 0:
                return False
    return True
def calculator(lattice):
    while not is_solve(lattice):
        changed = False
        for row in range(4):
            for col in range(4):
                if lattice[row][col] == 0:
                    row_value = check_row(lattice, row)
                    column_value = check_column(lattice, col)
                    block_value = check_block(lattice, col, row)
                    possible_num = row_value & column_value & block_value
                    #print(f"({row},{col}): row={row_value}, col={column_value}, block={block_value}, possible={possible_num}")
                    if len(possible_num) == 1:
                        value = list(possible_num)[0]
                        lattice[row][col] = value
                        changed = True
        if not changed:
            #print("無法填任何值，程式停止")
            break
   
def main():
    lattice = list()
    for _ in range(4):
        block = [int(m) for m in input().split()]
        lattice.append(block)
    calculator(lattice)
    for i in range(len(lattice)):
        for j in range(len(lattice[i])):
            print(lattice[i][j],end= " ")
        print()

if __name__ == "__main__":
    main()

