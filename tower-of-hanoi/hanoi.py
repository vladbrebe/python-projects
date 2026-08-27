"""Iterative Tower of Hanoi solver.

Rather than recursing, this uses the well-known iterative rule for the puzzle:

* On odd-numbered turns, move the smallest disk one fixed direction around the
  three rods. The direction depends on the parity of ``n``, which is what makes
  the pile end up on the third rod rather than the second.
* On even-numbered turns, exactly one legal move exists that does not involve
  the smallest disk. Make it.

That produces the optimal ``2**n - 1`` moves.
"""


def hanoi_solver(n):
    rods = [list(range(n, 0, -1)), [], []]
    states = [f"{rods[0]} {rods[1]} {rods[2]}"]

    # To move a pile of disks from the 1st pillar to the 3rd
    # you need to put the first disk on either the 2nd or 3rd pillar
    # depending on if n is even or odd
    if n%2:
        step = 2
    else:
        step =1

    # index of rod with smallest disk on it
    smallest_rod = 0

    # Moves the top item from the source pile to the target pile
    # At each game state there are only 3 valid moves:
    # - move the smallest disk to one of the two other spots
    # - move a disk from the top of one of the two other spots on top of the other
    # This solution proceeds by alternating between doing these two moves, which will provide
    # the optimal solution
    def move(source, target):
        rods[target].append(rods[source].pop())
        states.append(f"{rods[0]} {rods[1]} {rods[2]}")

    # A Tower of Hanoi solver can be implemented iteratively as follows
    for turn in range(1, 2 ** n):

        # On Odd turns always move smallest disk by a fixed amount
        if turn % 2 == 1:
            target = (smallest_rod + step) % 3
            move(smallest_rod, target)
            smallest_rod = target

        # Even turns
        else:
            a = (smallest_rod + 1) % 3 #right
            b = (smallest_rod - 1) % 3 #left

            # On even turns, first check if you can move a piece which
            # isn't the smallest to an empty spot
            if not rods[a]:
                move(b, a)
            elif not rods[b]:
                move(a, b)

            # Otherwise, move a disk to the only pillar it can fit on
            elif rods[a][-1] < rods[b][-1]:
                move(a, b)
            else:
                move(b, a)

    return "\n".join(states)



def main() -> None:
    disks = 3
    print(f"Tower of Hanoi with {disks} disks ({2**disks - 1} moves):")
    print(hanoi_solver(disks))


if __name__ == "__main__":
    main()
