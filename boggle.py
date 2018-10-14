'''Monica Erdman
Final project for Python for Programmers course

Play Boggle!!!
'''
        

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
        'Z':1}
    letters = []
    for i,j in letDist.items():
        letters.extend([i]*j)
    return letters

print(letter_assign())

n = 5
board = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(letter_select())
    board.append(row)

