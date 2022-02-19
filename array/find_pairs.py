# write a program to find all pairs of integers whose sum is equal to a given number (2, 2) and (3, 3) is not valid pairs
# leet code - two sums


def find_pairs(sequence, target):
    for i in range(len(sequence)):
        for j in range(1, len(sequence)):
            a = sequence[i]
            b = sequence[j]

            if a != b and (a + b == target):
                return (a, b)
    return "no pair found"



a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(find_pairs(a, 6))
print(find_pairs(a, 12))
print(find_pairs(a, 17))
print(find_pairs(a, 24))
