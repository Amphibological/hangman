''' A simple clone of hangman, implemented in Python.'''

import random
import blessings

CORRECT = 0
INCORRECT = 1
REPEAT = 2

with open('./wordlist.txt') as file:
    words = file.readlines().split()

def choose_word():
    return random.choice(words)

class Game():
    '''Represents a single iteration of a game of hangman.'''
    def __init__(self):
        self.word = choose_word()
        self.hidden_word = ['_'] * len(self.word)
        self.guessed = []
        self.mistakes_left = 10
    
    def guess(self, letter):
        '''Takes a letter guess and returns:
            0: guess is correct
            1: guess is incorrect
            2: guess has been done already
        '''
        if letter in self.word and letter not in self.guessed:
            indices = [i for i, x in enumerate(self.word) if x == letter]
            for index in indices:
                self.hidden_word[index] = letter
            return CORRECT
        elif letter in self.guessed:
            return REPEAT
        else:
            self.mistakes_left -= 1
            self.guessed += letter
            return INCORRECT