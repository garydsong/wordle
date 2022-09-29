# import stuff up here
from random import choice
from logo import logo
import os
from colorama import Fore, Back, Style


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
        # method to run the game logic (will call other methods)
        pass


    def update_display(self):
        # method to update the display in terminal on each guess
        pass


Wordle(5)
