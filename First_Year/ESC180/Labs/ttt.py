'''
 X | O | X
---+---+---
 O | O | X    
---+---+---
   | X | 
'''

import random
from copy import deepcopy

def human_v_human():
    O = False
    while(True):
        if(O):
            put_in_board(board, get_coord(int(input('Enter your move: '))), 'O')
            if(is_win(board, 'O')):
                break
        else:
            put_in_board(board, get_coord(int(input('Enter your move: '))), 'X')
            if(is_win(board, 'X')):
                break
        O = not O

        print_board_and_legend(board)
        print("\n\n")

    print_board_and_legend(board)
    if(O):
        print("O wins!")
    else:
        print("O loses!")

def human_v_computer():
    O = False
    while(True):
        if(O):
            print("Computer Move:")
            make_not_random_move(board, 'O')
            if(is_win(board, 'O')):
                break
        else:
            put_in_board(board, get_coord(int(input('Enter your move: '))), 'X')
            if(is_win(board, 'X')):
                break
        O = not O

        print_board_and_legend(board)
        print("\n\n")
    
    print_board_and_legend(board)
    if(O):
        print("O wins!")
    else:
        print("O loses!")


################################################################################


def print_board_and_legend(board):
    for i in range(3):
        line1 = " " +  board[i][0] + " | " + board[i][1] + " | " +  board[i][2]
        line2 = "  " + str(3*i+1)  + " | " + str(3*i+2)  + " | " +  str(3*i+3) 
        print(line1 + " "*5 + line2)
        if i < 2:
            print("---+---+---" + " "*5 + "---+---+---")
    
def make_empty_board():
    board = []
    for i in range(3):
        board.append([" "]*3)
    return board
    
def get_coord(square_num):
    ret = [(square_num - 1)// 3, (square_num % 3) - 1]
    if(ret[1] == -1):
        ret[1] = 2
    return ret

def put_in_board(board, location, char):
    validated = False

    if([location[0],location[1]] in get_free_board_squares(board)):
        validated = True

    while(not validated):
        location = get_coord(int(input("That space is not available. Enter an open space: ")))
        if([location[0],location[1]] in get_free_board_squares(board)):
            validated = True

    board[location[0]][location[1]] = char

def get_free_board_squares(board):
    ret = []
    for r in range(0, len(board)):
        for c in range(0, len(board[r])):
            if(board[r][c] == " "):
                ret.append([r,c])
    return ret

def make_random_move(board, mark):
    put_in_board(board, get_free_board_squares(board)[int(random.random() * len(get_free_board_squares(board))) // 1], mark)


def is_col_all_marks(board, col_i, mark):
    for r in board:
        if(r[col_i] != mark):
            return False
    return True 

def is_row_all_marks(board, row_i, mark):
    for c in board[row_i]:
        if c != mark: return False
    return True

def is_diagonals_all_marks(board, mark):
    return (board[1][1] == mark and ((board[0][0] == mark and board[2][2] == mark) or (board[0][2] == mark and board[2][0] == mark)))

def is_win(board, mark):
    for row_i in range(len(board)):
        if is_row_all_marks(board, row_i, mark):
            return True
    for col_i in range(len(board[0])):
        if is_col_all_marks(board, col_i, mark):
            return True
    if is_diagonals_all_marks(board, mark):
        return True
    return False

def other_mark(mark):
    if mark == 'O': return 'X'
    return 'O'

def make_not_random_move(board, mark):
    for e in get_free_board_squares(board):
        fake_board = deepcopy(board)
        put_in_board(fake_board, e, mark)
        if(is_win(fake_board, mark)):
            put_in_board(board, e, mark)
            return
    for e in get_free_board_squares(board):    
        fake_board = deepcopy(board)
        put_in_board(fake_board, e, other_mark(mark))
        if(is_win(fake_board, other_mark(mark))):
            put_in_board(board, e, mark)
            return

    make_random_move(board, mark)

if __name__ == '__main__':
    board = make_empty_board()
    print_board_and_legend(board)    
    
    print("\n\n")
    
    # board = [["O", "X", "X"],
    #          [" ", "X", " "],
    #          [" ", "O", " "]]

    human_v_computer()

