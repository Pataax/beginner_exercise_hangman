import pytest


def double():
    x = input("Enter an integer: ")
    return int(x)*2


def test_double(monkeypatch):
    var = (12, 24)

    for x in var:
        monkeypatch.setattr('builtins.input', lambda _: x)
        assert double() == x * 2
