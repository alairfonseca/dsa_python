def dot_product(list_a, list_b):
    len_a = len(list_a)
    len_b = len(list_b)

    if len_a != len_b:
        return

    result = [0] * len_a

    for i in range(0, len_a):
        result[i] = list_a[i] * list_b[i]

    return result


if __name__ == "__main__":
    list_a = [1, 2, 3, 4]
    list_b = [2, 2, 2, 2]

    print(dot_product(list_a, list_b))
    print(dot_product([1], [2, 2]))
