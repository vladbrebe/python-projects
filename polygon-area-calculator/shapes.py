"""
Rectangle and Square classes demonstrating inheritance.
"""



class Rectangle:

    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def set_width(self, width: float):
        self.width = width

    def set_height(self, height: float):
        self.height = height

    def get_area(self) -> float:
        return self.width * self.height

    def get_perimeter(self) -> float:
        return 2 * (self.width + self.height)

    def get_diagonal(self) -> float:
        return (self.width**2 + self.height**2) ** 0.5

    # returns a picture:str of the shape, for shapes up to side lengths of 50
    def get_picture(self) -> str:
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        return ("*"*self.width + "\n")*self.height

    # returns the integer amount of copies of 'shape' can fit inside 'self'
    def get_amount_inside(self, shape: Rectangle) -> int:
        return (self.width//shape.width)*(self.height//shape.height)

    def __str__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):

    def __init__(self, side: float) -> None:
        super().__init__(side, side)

    def set_width(self, width: float) -> None:
        self.set_side(width)

    def set_height(self, height: float) -> None:
        self.set_side(height)

    def set_side(self, side: float) -> None:
        self.width = side
        self.height = side

    def __str__(self) -> str:
        return f"Square(side={self.width})"


def main() -> None:
    """Run a short demonstration of both shapes."""
    rectangle = Rectangle(10, 5)
    print(rectangle)
    print(f"Area: {rectangle.get_area()}")
    rectangle.set_height(3)
    print(f"Perimeter after resize: {rectangle.get_perimeter()}")
    print(rectangle.get_picture())

    square = Square(9)
    print(square)
    print(f"Area: {square.get_area()}")
    square.set_side(4)
    print(f"Diagonal after resize: {square.get_diagonal():.4f}")
    print(square.get_picture())

    rectangle.set_width(16)
    rectangle.set_height(8)
    print(f"Squares of side 4 fit inside {rectangle}: {rectangle.get_amount_inside(square)}-times")


if __name__ == "__main__":
    main()
