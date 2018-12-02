'''Monica Erdman
Final project for Python for Programmers course

Play Boggle!!!
'''
 
import random, enchant, datetime

class Board():

    def __init__(self, size, letters):
        self.size = size
        self.board = self.create_board(self.size, letters)

#    def __init__(self, fixed_board):
#        size = len(fixed_board)
#        assert(size == len(fixed_board[0]))
#        self.size = size
#        self.board = fixed_board

    @classmethod
    def letter_select(cls, letters):
        l = random.randint(0,len(letters)-1)
        return letters[l]
    
    @classmethod
    def create_board(cls, size, letters):
        board = []
        for i in range(size):
            row = []
            for j in range(size):
                row.append(cls.letter_select(letters))
            board.append(row)
        return board
    
    def print(self):
        for row in range(len(self.board)):
            #print('+' + '––––-+'*len(board[0]))
            #print('|' + '     |'*len(board[0]))
            print()
            print(end=' ')
            for col in range(len(self.board[row])):
                print(' ', self.board[row][col], end = ' ')
            print(' ') #To change lines 
            #print('|' + '     |'*len(board[0]))
        #print('+' + '––-––+'*(len(board[0])))
        print()
    
    def find_first(self, word):
        start = []
        for i, row in enumerate(self.board):
            for j, x in enumerate(row):
                if x == word[0]:
                    indices = (i,j)
                    start.append(indices)
        return start
    
    def find_word(self, current_location, remaining_word, used_locations):
        letter = Letter(current_location, remaining_word[0])        
        if remaining_word[1:] == '':
            letter.children = None
            return letter
        else:
            used_locations.append(current_location) 
            next_letter = self.get_next_letter(current_location, remaining_word[1:], used_locations)
            for loc in next_letter:
                next_Letter = self.find_word(loc, remaining_word[1:], used_locations[:])
                if next_Letter != []:
                    letter.children.append(next_Letter)
                else:
                    pass
            if letter.children == []:
                return []
            else:
                return letter

    def get_next_letter(self, current_location, remaining_word, used_locations):
        i, j = current_location
        possible_locations = [(i-1,j-1),(i-1,j),(i-1,j+1),(i,j-1),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1)]
        filter_locations = [] #make sure locations are on the board
        for loc in possible_locations: 
            if loc[0] < self.size and loc[0] >= 0:
                if loc[1] < self.size and loc[1] >= 0:
                    filter_locations.append(loc)
                    
        valid_locations = [index for index in filter_locations if index not in used_locations]
        next_letter = []
        for index in valid_locations:
            if remaining_word[0] == self.board[index[0]][index[1]]:
                next_letter.append(index)
        return next_letter

class Letter():
    def __init__(self, current_location, character):
        self.location = current_location
        self.character = character
        self.children = []

    def __str__(self):
        return '({}, {}, {})'.format(self.location, self.character, self.children)

    def __repr__(self):
        return self.__str__()
        
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

def score(word):
    word_len = len(word)
    if word_len == 4:
        points = 1
    elif word_len == 5:
        points = 2
    elif word_len == 6:
        points = 3
    elif word_len == 7:
        points = 5
    elif word_len == 8:
        points = 11
    elif word_len > 8:
        points = word_len * 2
    return points
    
n = 5 #defines board size
game_time = datetime.timedelta(minutes=1)
d = enchant.Dict('en_US')
letters = letter_list()
myboard = Board(n, letters)
myboard.print()
points = 0
found_words = []

print('Time reminaing: 3 minutes')
start = datetime.datetime.now()
while datetime.datetime.now() < start + game_time:
    word = input('Type a word on the board:').upper()
    if len(word) > 3:
        check = d.check(word)
        if check == True:
            firsts = myboard.find_first(word)
            solutions = []
            used_locations = []
            for first in firsts:
                pot_soln = myboard.find_word(first, word, used_locations[:])
                if pot_soln == []:
                    pass
                else:
                    solutions.append(pot_soln)
            if solutions == []:
                print('Not on the board. Try again.')
            else:
                found_words.append(word)
        else:
            print('Not a word. Try again.')
    else:
        print('Word is too short. Try again')
print('Time\'s up')
for word in set(found_words):
    points += score(word)
print('Score: {}'.format(points))
print('Number of words found: {}'.format(len(set(found_words))))
