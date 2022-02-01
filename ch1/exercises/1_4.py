def squares_sum(n):
    result = 0

    for i in range(1, n):
        result += i ** 2

    return result


if __name__ == "__main__":
    print(squares_sum(5))
    print(squares_sum(10))
    print(squares_sum(30))
