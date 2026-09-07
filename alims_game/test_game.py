import pytest
from game_logic import check_guess


def test_check_guess_when_number_matches():
	assert check_guess(50, 50) == "win"


def test_check_guess_when_guess_is_greater():
	assert check_guess(50, 75) == "less"


def test_check_guess_when_guess_is_less():
	assert check_guess(50, 25) == "bigger"
5

