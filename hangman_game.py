"""
Hangman implementation by Kylie Ying
YouTube Kylie Ying: https://www.youtube.com/watch?v=8ext9G7xspg&t=1935s
Github: https://github.com/kying18/hangman/blob/master/hangman.py
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

    lives = 6

    while len(word_letters) > 0 and lives > 0:
        # letters used
        # " ".join(['a', 'b', 'c']) --> 'a b c'
        print(f"You have {lives} lives left")
        print("You have used this letters: ", ' '.join(used_letters))

        # what current word is (i.e W_RD)
        word_list = [
            letter if letter in used_letters else "_" for letter in word]
        print("Current word: ", ' '.join(word_list))

        user_attempt = input("Guess a letter: ").upper()
        if user_attempt in alphabet - used_letters:
            used_letters.add(user_attempt)
            if user_attempt in word_letters:
                word_letters.remove(user_attempt)
            else:
                lives = lives - 1
                print(f"You letter {user_attempt} is not in the word")
        elif user_attempt in used_letters:
            print("You have already used that letter. Try another letter.")
        else:
            print("Invalid character. That is not a valid letter. Please try again")

    if lives == 0:
        print(f"You died, sorry. The word was {word}")
    else:
        print(f"You guessed the word {word}!")


if __name__ == "__main__":
    hangman()
