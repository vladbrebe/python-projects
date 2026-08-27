import pytest

from shapes import Rectangle, Square


def test_rectangle_measurements():
    rectangle = Rectangle(10, 5)
    assert rectangle.get_area() == 50
    assert rectangle.get_perimeter() == 30
    assert rectangle.get_diagonal() == pytest.approx(11.180339887498949)


def test_rectangle_picture():
    assert Rectangle(3, 2).get_picture() == "***\n***\n"


def test_picture_refuses_oversized_shapes():
    assert Rectangle(51, 2).get_picture() == "Too big for picture."


def test_square_is_a_rectangle():
    assert isinstance(Square(4), Rectangle)


def test_square_setters_keep_sides_equal():
    square = Square(9)
    square.set_width(4)
    assert (square.width, square.height) == (4, 4)
    square.set_height(7)
    assert (square.width, square.height) == (7, 7)
    square.set_side(2)
    assert (square.width, square.height) == (2, 2)


def test_amount_inside():
    rectangle = Rectangle(16, 8)
    assert rectangle.get_amount_inside(Square(4)) == 8


def test_str_representations():
    assert str(Rectangle(10, 3)) == "Rectangle(width=10, height=3)"
    assert str(Square(5)) == "Square(side=5)"
