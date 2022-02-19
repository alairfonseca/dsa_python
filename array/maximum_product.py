# find maximum product of two integers in the array where all elements are positive


def find_maximum_product(sequence):
    maximum_product = 0

    for i in sequence:
        for j in sequence[1:]:
            product = i * j

            if product > maximum_product:
                maximum_product = product

    return maximum_product


print(find_maximum_product([1, 2, 3, 4, 5, 6, 7, 8, 9]))
