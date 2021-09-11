"""
Hangman implementation by Kylie Ying
YouTube Kylie Ying: https://www.youtube.com/watch?v=8ext9G7xspg&t=1935s
"""

import random
import string
from database import words


def get_valid_word(data):
    word = random.choice(data)  # randomly chooses something from the list
    while ('-' in word) or (' ' in word):
        word = random.choice(data)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has already tried

    user_attempt = input("Guess a letter: ").upper()
    if user_attempt in alphabet - used_letters:
        used_letters.add(user_attempt)
        if user_attempt in word_letters:
            word_letters.remove(user_attempt)
    elif user_attempt in used_letters:
        print("You have already used that character. Please try again.")
    else:
        print("Invalid character. Please try again.")


if __name__ == "__main__":
    hangman()
