import pytest
import hangman_game
from database import words
from hangman_game import get_valid_word, hide_word, hangman


def test_get_valid_word_returns_only_simple_words():
    for i in range(10):
        word = get_valid_word(words)
        assert "-" not in word
        assert " " not in word
        assert "_" not in word


def test_hide_word_return_underscore_when_used_letters_empty(monkeypatch):
    test_word = "return"
    monkeypatch.setattr(hangman_game, 'used_letters', {})
    assert hide_word(test_word) == "_ _ _ _ _ _"


def test_hide_word_return_some_letter_when_used_letter_not_empty(monkeypatch):
    test_word = "return"
    monkeypatch.setattr(hangman_game, 'used_letters', {"R", "T"})
    assert hide_word(test_word) == "R _ T _ R _"


def test_when_word_letters_is_0(monkeypatch, capsys):
    hangman('')

    captured_stdout, captured_stderr = capsys.readouterr()
    captured_stdout = captured_stdout.strip()
    assert captured_stdout == "You guessed the word !"


def test_when_lives_is_0(monkeypatch, capsys):
    monkeypatch.setattr(hangman_game, 'PLAYER_LIVES', 0)

    chosen_word = get_valid_word(words)
    hangman(chosen_word)

    captured_stdout, captured_stderr = capsys.readouterr()
    captured_stdout = captured_stdout.strip()
    assert captured_stdout == f"You died, sorry. The word was {chosen_word}"


def test_user_input_is_quit(monkeypatch, capsys):
    def user_input(_): return "quit"
    monkeypatch.setattr('builtins.input', user_input)

    chosen_word = get_valid_word(words)
    hidden_word = hide_word(chosen_word)
    hangman(chosen_word)

    captured_stdout, captured_stderr = capsys.readouterr()
    captured_stdout = captured_stdout.strip()
    captured_stdout = captured_stdout.replace("\n", '')
    captured_stdout = captured_stdout.replace("Lives left: 6", '')
    captured_stdout = captured_stdout.replace(
        f"Current word: {hidden_word}", '')
    assert captured_stdout == "You choose to leave the game"


# def test_repeated_letter(monkeypatch):
#     def user_input(_): return "a"
#     monkeypatch.setattr('builtins.input', user_input)

#     chosen_word = get_valid_word("DANGER")
#     # hidden_word = hide_word(chosen_word)
#     hangman(chosen_word)
#     assert hangman_game.used_letters == {"A"}


# error - infinite loop
# def test_user_input_is_not_alpha(monkeypatch, capsys):
#     input_list = ["1", "quit"]

#     for char in input_list:
#         monkeypatch.setattr('builtins.input', lambda _: char)

#         chosen_word = get_valid_word(words)
#         # hidden_word = hide_word(chosen_word)
#         hangman(chosen_word)

#         captured_stdout, captured_stderr = capsys.readouterr()
#         captured_stdout = captured_stdout.strip()
#         assert captured_stdout == "Invalid character. That is not a valid letter. Please try again"
