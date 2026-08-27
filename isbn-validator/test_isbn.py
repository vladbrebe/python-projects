import pytest

from isbn import calculate_check_digit_10, calculate_check_digit_13, validate_isbn

# validate_isbn prints its result and returns None, so these tests use pytest's
# built-in capsys fixture to capture what was printed.


def test_valid_isbn_10(capsys):
    validate_isbn("1530051126", 10)
    assert capsys.readouterr().out == "Valid ISBN Code.\n"


def test_valid_isbn_13(capsys):
    validate_isbn("9781530051120", 13)
    assert capsys.readouterr().out == "Valid ISBN Code.\n"


def test_invalid_isbn_10(capsys):
    validate_isbn("1530051127", 10)
    assert capsys.readouterr().out == "Invalid ISBN Code.\n"


def test_invalid_isbn_13(capsys):
    validate_isbn("9781530051121", 13)
    assert capsys.readouterr().out == "Invalid ISBN Code.\n"


def test_check_digit_x_is_accepted(capsys):
    # 043942089X is a real ISBN-10 whose check digit is the letter X.
    validate_isbn("043942089X", 10)
    assert capsys.readouterr().out == "Valid ISBN Code.\n"


def test_lower_case_x_is_rejected(capsys):
    # The comparison is case sensitive, so a lower-case x does not match.
    validate_isbn("043942089x", 10)
    assert capsys.readouterr().out == "Invalid ISBN Code.\n"


def test_wrong_length_prints_a_message(capsys):
    validate_isbn("15300511", 10)
    assert capsys.readouterr().out == "ISBN-10 code should be 10 digits long.\n"


def test_non_numeric_digits_raise_value_error():
    # int() rejects the letter, and validate_isbn does not catch it.
    # main() is what turns this into a message for the user.
    with pytest.raises(ValueError):
        validate_isbn("15300511A6", 10)


def test_calculate_check_digit_10():
    assert calculate_check_digit_10([1, 5, 3, 0, 0, 5, 1, 1, 2]) == "6"
    assert calculate_check_digit_10([0, 4, 3, 9, 4, 2, 0, 8, 9]) == "X"


def test_calculate_check_digit_13():
    assert calculate_check_digit_13([9, 7, 8, 1, 5, 3, 0, 0, 5, 1, 1, 2]) == "0"
