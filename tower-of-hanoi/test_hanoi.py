import pytest

from hanoi import hanoi_solver


# hanoi_solver returns text, so these helpers read the rods back out of it.
# Each line looks like "[3, 2, 1] [] []": splitting on "] [" separates the
# three rods, and stripping the outer brackets leaves the disk numbers.


def test_one_disk():
    assert hanoi_solver(1) == "[1] [] []\n[] [] [1]"


def test_two_disks():
    assert hanoi_solver(2) == "[2, 1] [] []\n[2] [1] []\n[] [1] [2]\n[] [] [2, 1]"


def test_three_disks():
    lines = [
        "[3, 2, 1] [] []",
        "[3, 2] [] [1]",
        "[3] [2] [1]",
        "[3] [2, 1] []",
        "[] [2, 1] [3]",
        "[1] [2] [3]",
        "[1] [] [3, 2]",
        "[] [] [3, 2, 1]",
    ]
    assert hanoi_solver(3) == "\n".join(lines)


def test_starts_with_every_disk_on_the_first_rod():
    assert hanoi_solver(4).split("\n")[0] == "[4, 3, 2, 1] [] []"


def test_finishes_with_every_disk_on_the_third_rod():
    assert hanoi_solver(4).split("\n")[-1] == "[] [] [4, 3, 2, 1]"


def test_number_of_moves_is_optimal():
    for n in range(1, 8):
        line_count = len(hanoi_solver(n).split("\n"))
        assert line_count == 2**n
