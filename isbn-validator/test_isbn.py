import pytest

from isbn import calculate_check_digit_10, calculate_check_digit_13, validate_isbn


def test_valid_isbn_10():
    assert validate_isbn("1530051126", 10) is True


def test_valid_isbn_13():
    assert validate_isbn("9781530051120", 13) is True


def test_invalid_check_digit():
    assert validate_isbn("1530051127", 10) is False
    assert validate_isbn("9781530051121", 13) is False


def test_check_digit_helpers():
    assert calculate_check_digit_10([1, 5, 3, 0, 0, 5, 1, 1, 2]) == "6"
    assert calculate_check_digit_13([9, 7, 8, 1, 5, 3, 0, 0, 5, 1, 1, 2]) == "0"


def test_wrong_length_raises():
    with pytest.raises(ValueError, match="should be 10 digits long"):
        validate_isbn("15300511", 10)


def test_unsupported_length_raises():
    with pytest.raises(ValueError, match="Length should be 10 or 13"):
        validate_isbn("123456789012", 12)


def test_non_numeric_body_raises_instead_of_crashing():
    with pytest.raises(ValueError, match="Invalid character was found"):
        validate_isbn("15300511A6", 10)
