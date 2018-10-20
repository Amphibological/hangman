''' A simple clone of hangman, implemented in Python.'''

import time
import random
from blessings import Terminal

CORRECT = 0
INCORRECT = 1
REPEAT = 2

term = Terminal()

with open('./wordlist.txt') as file:
    words = [s.strip() for s in file.readlines()]

def choose_word():
    return random.choice(words).upper()

class Game():
    '''Represents a single iteration of a game of hangman.'''
    def __init__(self, guesses=10):
        self.word = choose_word()
        self.hidden_word = ['_'] * len(self.word)
        self.guessed = []
        self.mistakes_left = guesses
    
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
        elif letter in self.guessed or letter in self.hidden_word:
            return REPEAT
        else:
            self.mistakes_left -= 1
            self.guessed += letter
            return INCORRECT
    
    def print_state(self):
        '''Pretty print the current game state:
        Current Word: __D____R
        Guessed: HFKL
        Wrong guesses left: 6
        '''
        print()
        print(f"Current Word: {''.join(self.hidden_word)}")
        # print(f"HIDDEN WORD: {self.word}")  # For debug only TODO remove
        print(f"Guessed: {' '.join(self.guessed)}")
        print(f'Wrong guesses left: {self.mistakes_left}')


def main():
    print(term.enter_fullscreen)
    game = Game()
    while True:
        print(term.clear + term.move(0, 0))
        game.print_state()
        inp = input('Please enter a single letter guess or quit to exit: ')
        if inp.lower() == 'quit':
            print()
            print('Bye!')
            time.sleep(0.2)
            break
        if len(inp) != 1:
            print(term.bold_yellow('Please enter only a single letter!'))
            time.sleep(0.7)
            continue
        letter = inp.upper()
        guess = game.guess(letter)
        if guess == CORRECT:
            print(term.bold_green('Good job!'))
            if '_' not in game.hidden_word:
                print()
                print("Congrats, you've won!")
                print(f'The word was {game.word}')
                time.sleep(2)
                break
            time.sleep(0.7)
            continue
        elif guess == REPEAT:
            print(term.bold_yellow("You've already tried that letter!"))
            time.sleep(0.7)
            continue
        elif guess == INCORRECT:
            print(term.bold_red('Sorry, not the right letter!'))
            if not game.mistakes_left:
                print()
                print('Game Over!')
                print(f'The word was {game.word}!')
                time.sleep(2)
                break
            time.sleep(0.7)
            continue
    print(term.exit_fullscreen)


if __name__ == '__main__':
    main()