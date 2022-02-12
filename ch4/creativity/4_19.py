"""
Write a short recursive Python function that rearranges a sequence of integer
values so that all the even values appear before all the odd values.
"""


def order_by_even(sequence):
    if len(sequence) == 1:
        return sequence
    if sequence[0] % 2 == 0:
        return [sequence[0]] + order_by_even(sequence[1:])
    else:
        aux = sequence[0]
        del sequence[0]
        sequence.append(aux)

        return order_by_even(sequence[:-1]) + sequence[-1:]


if __name__ == "__main__":
    print("-----------------------------------------------")
    print(order_by_even([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    print(order_by_even([2, 2, 3, 3, 4, 4, 5, 6, 7, 8, 9]))
    print(order_by_even([12, 21, 33, 45, 56, 67, 78, 89, 90]))
