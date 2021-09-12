"""
Hangman implementation by Kylie Ying
YouTube Kylie Ying: https://www.youtube.com/watch?v=8ext9G7xspg&t=1935s
Github: https://github.com/kying18/hangman/blob/master/hangman.py
"""

import random
import time
from database import words


PLAYER_LIVES = 6
SEPARATOR = "=" * 50

used_letters = set()  # what the user has already tried


def get_valid_word(data):
    word = random.choice(data)  # randomly chooses something from the list
    while ('-' in word) or (' ' in word):
        word = random.choice(data)
    return word.upper()


def hide_word(word):
    global used_letters

    word_list = []
    for letter in word:
        if letter.upper() in used_letters:
            word_list.append(letter.upper())
        else:
            word_list.append("_")
    return " ".join(word_list)


def hangman(word):
    word_letters = set(word)  # letters in the word
    lives = PLAYER_LIVES

    while len(word_letters) > 0 and lives > 0:
        hidden_word = hide_word(word)
        print(f"Lives left: {lives}")
        print(f"Current word: {hidden_word}")
        time.sleep(1.1)

        user_attempt = input("Guess a letter: ").upper()

        if user_attempt == "QUIT":
            print("You choose to leave the game")
            break
        elif (user_attempt.isalpha()) and (user_attempt not in used_letters):
            used_letters.add(user_attempt)
            if user_attempt in word_letters:
                word_letters.remove(user_attempt)
                time.sleep(1.1)
            else:
                lives = lives - 1
                time.sleep(1.1)
                print(f"You letter {user_attempt} is not in the word")
                time.sleep(1.1)
        elif user_attempt in used_letters:
            time.sleep(1.1)
            print("You have already used that letter. Try another letter.")
            time.sleep(1.1)
        else:
            time.sleep(1.1)
            print("Invalid character. That is not a valid letter. Please try again")
            time.sleep(1.1)
        print(SEPARATOR)

    if lives == 0:
        time.sleep(1.1)
        print(f"You died, sorry. The word was {word}")
    elif len(word_letters) == 0:
        time.sleep(1.1)
        print(f"You guessed the word {word}!")


def start():
    print(SEPARATOR)
    time.sleep(1)
    print("Hangman Game")
    time.sleep(1.1)
    print(f"Try to guess the word...")
    time.sleep(1.1)
    print(f"... or die trying. Good luck!")
    time.sleep(2)
    print(SEPARATOR)

    chosen_word = get_valid_word(words)
    hangman(chosen_word)


if __name__ == "__main__":
    start()
