# import stuff up here
from random import choice
from logo import logo
import os
from colorama import Back, Style


class Wordle:
    def __init__(self, letters=5, logo=logo):
        self._letters = letters
        self._logo = logo
        self._guess = ''
        self._guesses = [[] for x in range(6)]
        self._tries = 0
        self._words = self.get_all_words()
        self._game_word = self.chose_game_word()
        self.play_game()


    def get_all_words(self):
        f = open("words.txt", "r")
        words = [ line.rstrip() for line in f ]
        wordle_words = [ word for word in words if len(word) == self._letters]
        return wordle_words


    def chose_game_word(self):
        return choice(self._words)


    def guess(self):
        bad_guess = True
        while bad_guess:
            user_guess = input(f"Guess a {self._letters} letter word: ").lower()
            if len(user_guess) != self._letters:
                print(f"Words must be {self._letters} letters.")
                continue
            elif user_guess in self._guesses:
                print(f"You have already guessed {user._guess}")
                continue
            else:
                bad_guess = False
                self._guess = user_guess
                self._guesses[self._tries] = self._guess
                self._tries += 1


    def play_game(self):
        print(self._logo)
        print('Welcome to Wordle!')
        while self._tries < 6:
            self.guess()
            self.update_display()
            if self._guess == self._game_word:
                print(f"You've done it! {self._tries}/5 tries. The word was {self._game_word.upper()}")
                return
        print(f"You've ran out of tries. The word was {self._game_word.upper()}")


    def update_display(self):
        os.system('clear')
        for word in self._guesses:
            if len(word) > 0:
                display = []
                for index, letter in enumerate(word):
                    if letter == self._game_word[index]:
                        display.extend([Back.GREEN, letter.upper(), Style.RESET_ALL, ' '])
                    elif letter in self._game_word and letter != self._game_word[index]:
                        display.extend([Back.YELLOW, letter.upper(), Style.RESET_ALL, ' '])
                    else:
                        display.extend([Style.RESET_ALL, letter.upper(), Style.RESET_ALL, ' '])
                for index, word in enumerate(display):
                    if index == (len(display) - 1):
                        print(word)
                    else:
                        print(word, end='')

            else:
                display = [ "_" for x in range(len(self._game_word))]
                print(' '.join(display))


Wordle(5)
