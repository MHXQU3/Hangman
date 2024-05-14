import random
from turtle import position
import string

visual = [
    '________',
    '|/     |',
    '|      O',
    '|     /|\ ',
    '|     / \ '
    '\n|\______'
]

class Hangman:

    def __init__(self, word_list, num_lives=6):
      self.num_lives = num_lives
      self.word_list = word_list
      word_list = ['apple', 'banana', 'dog', 'orange', 'melon',
    'read', 'dance', 'happy', 'guitar', 'football', 'novel', 'piano',
    'elephant', 'dolphin', 'electric', 'crocodile', 'hurricane']
      self.chosen_word = random.choice(self.word_list)
      self.word_guessed = list(('_')) * len(self.chosen_word)
      self.list_letters = []
      self.num_letters = len(set(self.chosen_word))
      self.attempts = 0
      print ('The mystery word has', len(self.chosen_word), 'characters')
      print (self.word_guessed)

    def check_letter(self, letter):
        letter = letter.lower()
        if letter in self.chosen_word:
        
            for position, char in enumerate(self.chosen_word):
                if char == letter:
                    self.word_guessed[position] = letter
            self.num_letters -= 1
            print(self.word_guessed)
        else:
            self.num_lives -= 1
            self.attempts += 1
            print ('That was an incorrect guess')
            print ('\nYou have', self.num_lives , 'lives remaining')
            print ('\n'.join(visual[:self.attempts]))
        
        self.list_letters.append(letter)

    def ask_letter(self):
        letter = input ('please enter a letter: ') 

        if len(letter) != 1 or not letter.isalpha() :
            print ('Sorry, your input was not valid')
        
        elif letter in self.list_letters:
            print ('Oops! You have already guessed that letter')

        else:
            self.check_letter(letter)
        
        pass
   

def play_game (word_list):

        game = Hangman (word_list, num_lives=6)
        while True:
            if game.num_lives == 0:
                print (f'You have no more lives remaining. \nThe word you were looking for was {game.chosen_word}')
                break
            elif game.num_letters > 0:
                game.ask_letter()

            else:
                print ('You have guessed the word. Congratulations!')
                break

            pass


if __name__ == '__main__':
    word_list = ['apple', 'pear', 'banana', 'strawberry', 'watermelon', 'orange']
    play_game(word_list)

        
