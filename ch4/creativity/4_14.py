"""
In the Towers of Hanoi puzzle, we are given a platform with three pegs,
a, b, and c, sticking out of it. On peg a is a stack of n disks, each larger
than the next, so that the smallest is on the top and the largest is on the
bottom. The puzzle is to move all the disks from peg a to peg c, moving one
disk at a time, so that we never place a larger disk on top of a smaller one.
See Figure 4.15 for an example of the case n = 4. Describe a recursive algorithm
for solving the Towers of Hanoi puzzle for arbitrary n. (Hint: Consider first the
subproblem of moving all but the nth disk from peg a to another peg using the
third as 'temporary storage.')
"""


def hanoi_tower(n, from_peg, to_peg, aux_peg):
    if n == 0:
        print("move disk 1 from peg", from_peg, "to peg", to_peg)
        return
    hanoi_tower(n - 1, from_peg, aux_peg, to_peg)
    print("move disk", n, "from peg", from_peg, "to peg", to_peg)
    hanoi_tower(n - 1, aux_peg, to_peg, from_peg)


if __name__ == "__main__":
    print(hanoi_tower(4, 'a', 'c', 'b'))
