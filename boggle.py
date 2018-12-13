'''
Monica Erdman
Final project for UCSC Python for Programmers course

Play Boggle!!!
'''
 
import random, enchant, datetime

class Board():

    def __init__(self, size, letters):
        self.size = size
        self.board = self.create_board(self.size, letters)

    @classmethod    #randomized selection of letters from a set list
    def letter_select(cls, letters):
        l = random.randint(0,len(letters)-1)
        return letters[l]
    
    @classmethod    #selects letters to form a boggle board of a defined size
    def create_board(cls, size, letters):
        board = []
        for i in range(size):
            row = [cls.letter_select(letters) for j in range(size)]
            board.append(row)
        return board
    
    def print(self):    #prints the board to the screen with letters spaced in a grid
        for row in range(len(self.board)):
            print()
            print(end=' ')
            for col in range(len(self.board[row])):
                print(' ', self.board[row][col], end = ' ')
            print(' ') #To change lines 
        print()
    
    def find_first(self, word): #finds the locations of the first letter in the user-derived word
        start = []
        for i, row in enumerate(self.board):
            for j, x in enumerate(row):
                if x == word[0]:
                    indices = (i,j)
                    start.append(indices)
        return start
    
    def find_word(self, current_location, remaining_word, used_locations):
        '''
        Uses recursion to find the user-derived word on the boggle board;
        Makes use of try-except in case an untested error case occurs
        '''
        try:
            letter = Letter(current_location, remaining_word[0])        
            if remaining_word[1:] == '':    #when at the end of the word
                letter.children = None
                return letter
            else:                           #when letters are left to be found in the word
                used_locations.append(current_location) #no re-using letters
                next_location = self.get_next_letter(current_location, remaining_word[1:], used_locations)
                for loc in next_location:
                    #recurse
                    next_Letter = self.find_word(loc, remaining_word[1:], used_locations[:])
                    if next_Letter != []:   #when the next letter is found, stores children
                        letter.children.append(next_Letter)
                    else:                   #when the next letter doesn't exist
                        pass
                if letter.children == []:   #only returns a solution if the whole word is found
                    return []
                else:
                    return letter
        except Exception as e:
            print('Unexpected error. The error message is', e)

    def get_next_letter(self, current_location, remaining_word, used_locations):
    #finds the location(s) of the next letter in the word
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

class Letter(): #used to create linked list of class Letters and subsequent Letters
    def __init__(self, current_location, character):
        self.location = current_location
        self.character = character
        self.children = []

    def __repr__(self): #defines how to print Letters
        return '({}, {}, {})'.format(self.location, self.character, self.children)
        
def letter_list():  #letter distribution of scrabble
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
    lst = [[i]*j for i,j in letDist.items()]
    letters = [x for sublist in lst for x in sublist]
    return letters

def score(word):    #tallies the score
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
mins = 3 #defines the game length, in minutes
game_time = datetime.timedelta(minutes=mins)
d = enchant.Dict('en_US')   #valid words are English words
letters = letter_list()
myboard = Board(n, letters)
myboard.print()
points = 0
found_words = []

print('Time remaining: {} minutes'.format(mins))
start = datetime.datetime.now()
while datetime.datetime.now() < start + game_time:
    word = input('Type a word on the board: ').upper()
    if len(word) > 3:   #defines minimal word length
        check = d.check(word)   #check if input is a word first
        if check == True:   #if it's a word, find it on the board
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
                print('Not on the board. Try again.')   #when word doesn't exist on the board
            else:
                if word in found_words:
                    print('You already found this word. Try again.')    #inform user when word has already been found
                else:
                    found_words.append(word)    #catch all the found words
        else:
            print('Not a word. Try again.') #when input is not a word
    else:
        print('Word is too short. Try again')   #when input word length is too short
print('Time\'s up')
for word in set(found_words):   #don't score words twice
    points += score(word)
print('Score: {}'.format(points))
print('Number of words found: {}'.format(len(set(found_words))))
