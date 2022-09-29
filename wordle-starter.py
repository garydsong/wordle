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
        # method to pick a random word to play with
        pass


    def guess(self):
        # method to handle user input for guesses
        pass


    def play_game(self):
        # method to run the game logic (will call other methods)
        pass


    def update_display(self):
        # method to update the display in terminal on each guess
        pass


Wordle(5)
