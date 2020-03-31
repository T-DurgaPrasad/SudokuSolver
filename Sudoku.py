#--------Global Variables-----------

# Input Board
board =[
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
]




'''
# Take User Keys To Solve
def get_keys():
    is_done = True
    print("If You Are Done Adding Keys enter [ row = -1 col= -1 key =-1 ] ")
    while is_done:
        x, y, k = map(int, input("Enter The Position And Key // Note i/p format :[ row[1-9] col[1-9]  key[1-9]] // : ").split( ))
        if x == y == k == -1:
            break
        x -= 1
        y -= 1
        if is_valid(x,y):
            print(" Oop's Invalid Position!..")
            continue
        elif is_a_valid_key(k,(x,y)):
            print(" Oop's Invalid Key!..")
            continue

        if board[x][y] != 0:
            print("Do You Want To OverWrite ", "[", x+1, "]", "[", y+1, "] : ",   board[x][y])
            status = input("YES For Y|y and NO For N|n :")
            if status == 'N' or status == 'n':
                continue
        board[x][y] = k

    print("- - - - Given  - - - -")
    print_board()

'''


def is_valid_input():
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != 0:
                if not input_match_valid(board[i][j], (i, j)):
                    print(is_a_valid_key(board[i][j], (i, j)))
                    print(board[i][j], " ", i+1, " ", j+1)
                    return False
    return True


# Input Validation
def input_match_valid(key, pos):
    # Key Validation
    if key < 1 or key > 9:
        print("Invalid Key At : ", key, " ", pos[0]+1, " ", pos[1]+1 )
        return False
    # Row Checking
    for i in range(len(board[pos[1]])):
        if board[pos[0]][i] == key and pos[1] != i:
            print("Row Match At (value, row, col ): ")
            print(key, " ", pos[0]+1 , " " , pos[1]+1)
            print(key, " ", pos[0]+1 , " " , i+1)
            return False

    # column Checking
    for i in range(len(board)):
        if board[i][pos[1]] == key and pos[0] != i:
            print("Column Match At (value, row, col ): ")
            print(key, " ", pos[0]+1, " ", pos[1]+1)
            print(key, " ", i+1, " ", pos[1]+1)
            return False
    # Box Checking
    xx = pos[0] // 3
    yy = pos[1] // 3
    for i in range(xx * 3, xx * 3 + 3):
        for j in range(yy * 3, yy * 3 + 3):
            if i != pos[0] and j != pos[1] and board[i][j] == key:
                print("Box Match At (value, row, col ): ")
                print(key, " ", pos[0]+1, " ", pos[1]+1)
                print(key, " ", i+1, " ", j+1)
                return False
    return True


def solve():
    empty_cell = get_empty()
    if not empty_cell:                 # If Not Found Any Empty Cells Then We Get The Solution
        return True
    else:
        row,col = empty_cell
        for i in range(1, 10):
            if is_a_valid_key(i, (row, col)):
                board[row][col] = i
                if solve():
                    return True
                board[row][col] = 0
        return False


# Return The Empty Cell
def get_empty():
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return (i, j)            # row , Column


# Position Validation
def is_valid(x, y):

    if 0 > x > 8 and 0 > y > 8:
        return True
    else:
        return False


# Key Validation
def is_a_valid_key(key, pos):

    # Key Validation
    if key < 1 or key > 9:
        return False
    # Row Checking
    for i in range(len(board[pos[1]])):
        if board[pos[0]][i] == key and pos[1] != i:
            return False

    # Column Checking
    for i in range(len(board)):
        if board[i][pos[1]] == key and pos[0] != i:
            return False
    # Box Checking
    xx = pos[0] // 3
    yy = pos[1] // 3
    for i in range(xx * 3, xx * 3 + 3):
        for j in range(yy * 3, yy * 3 + 3):
            if i != pos[0] and j != pos[1] and board[i][j] == key:
                return False
    return True



# Prints The Board
def print_board(board):
    # print("- - - - Sudoku  - - - -")
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")



# Main Call Starts Hear

print("- - - - Given  - - - -")
print_board(board)
temp_board = board
if not is_valid_input():
    print()
    print("- - - InValid input - -")
    print_board(temp_board)
elif solve():
    print()
    print("- - - - Solution - - - -")
    print_board(board)
else:
    print()
    print("--Solution Not Exists--")
    print_board(temp_board)




'''

- - - - Given  - - - -
7 8 0  | 4 0 0  | 1 2 0
6 0 0  | 0 7 5  | 0 0 9
0 0 0  | 6 0 1  | 0 7 8
- - - - - - - - - - - - 
0 0 7  | 0 4 0  | 2 6 0
0 0 1  | 0 5 0  | 9 3 0
9 0 4  | 0 6 0  | 0 0 5
- - - - - - - - - - - - 
0 7 0  | 3 0 0  | 0 1 2
1 2 0  | 0 0 7  | 4 0 0
0 4 9  | 2 0 6  | 0 0 7


- - - - Solution - - - -
7 8 5  | 4 3 9  | 1 2 6
6 1 2  | 8 7 5  | 3 4 9
4 9 3  | 6 2 1  | 5 7 8
- - - - - - - - - - - - 
8 5 7  | 9 4 3  | 2 6 1
2 6 1  | 7 5 8  | 9 3 4
9 3 4  | 1 6 2  | 7 8 5
- - - - - - - - - - - - 
5 7 8  | 3 9 4  | 6 1 2
1 2 6  | 5 8 7  | 4 9 3
3 4 9  | 2 1 6  | 8 5 7

'''