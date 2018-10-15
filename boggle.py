'''Monica Erdman
Final project for Python for Programmers course

Play Boggle!!!
'''
 
import random

def letter_list():
    letDist = {
        'A':9,
        'B':2,
        'C':2,
        'D':4,
        'E':12,
        'F':2,
        'G':3,
        'H':2,
        'I':9,
        'J':1,
        'K':1,
        'L':4,
        'M':2,
        'N':6,
        'O':8,
        'P':2,
        'Q':1,
        'R':6,
        'S':4,
        'T':6,
        'U':4,
        'V':2,
        'W':2,
        'X':1,
        'Y':2,
        'Z':1  }
    letters = []
    for i,j in letDist.items():
        letters.extend([i]*j)
    return letters

def letter_select(letters):
    l = random.randint(0,len(letters)-1)
    return letters[l]

def create_board(n, letters):
    board = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(letter_select(letters))
        board.append(row)
    return board

def print_board(board):
    for row in range(len(board)):
        print('+' + '––––-+'*len(board[0]))
        print('|' + '     |'*len(board[0]))
        print('|', end='')
        for col in range(len(board[row])):
            print(' ',board[row][col], end='  |')
        print(' ') #To change lines 
        print('|' + '     |'*len(board[0]))
    print('+' + '––-––+'*(len(board[0])))
    

n = 5 #defines board size
board = create_board(n, letter_list())
print_board(board)
