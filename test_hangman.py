import pytest
from io import StringIO
from database import words
from hangman_game import get_valid_word, hangman


def test_get_valid_word_returns_only_simple_words():
    for i in range(10):
        word = get_valid_word(words)
        assert "-" not in word
        assert " " not in word


def test_hangman_only_accept_letters(monkeypatch, capsys):
    input_list = ["1", "!", " "]

    for x in input_list:
        user_input = StringIO(x + '\n')
        monkeypatch.setattr('sys.stdin', user_input)

        hangman()
        captured_stdout, captured_stderr = capsys.readouterr()
        captured_stdout = captured_stdout.strip().replace("Guess a letter: ", "")
        assert captured_stdout == "Invalid character. Please try again."
