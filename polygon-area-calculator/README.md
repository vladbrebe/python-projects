# Polygon Area Calculator

`Rectangle` and `Square` classes, where `Square` inherits from `Rectangle`.

## Design notes

The interesting question here is how a `Square` stays square. A square *is* a
rectangle, so inheritance is the natural relationship, but `Rectangle` exposes
`set_width` and `set_height` independently. Calling `set_width(5)` on a square
of side 3 would leave an object that claims to be a `Square` while being 5 by 3.

`Square` therefore overrides both setters so each one sets *both* sides, with
`set_side` as the single method they delegate to. The invariant is enforced in
one place rather than three.

This is a small, concrete instance of the Liskov substitution principle: the
subclass has to keep working wherever the parent class is expected, which means
it cannot simply inherit setters that break its own invariant.

## Methods

| Method | Returns |
| --- | --- |
| `get_area()` | Width times height |
| `get_perimeter()` | Twice the sum of the sides |
| `get_diagonal()` | Length of the diagonal |
| `get_picture()` | ASCII drawing, or a notice if a side exceeds 50 |
| `get_amount_inside(shape)` | How many copies of `shape` tile inside |

## Run it

```bash
python shapes.py
```

## Sample output

```
Rectangle(width=10, height=5)
Area: 50
Perimeter after resize: 26
**********
**********
**********

Square(side=9)
Area: 81
Diagonal after resize: 5.6569
****
****
****
****

Squares of side 4 inside Rectangle(width=16, height=8): 8
```

## Tests

```bash
pytest test_shapes.py
```
