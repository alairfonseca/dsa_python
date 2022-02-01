def odd_squares_sum(n):
    result = 0

    for i in range(1, n):
        if i % 2 == 0:
            result += i ** 2

    return result


if __name__ == "__main__":
    print(odd_squares_sum(5))
    print(odd_squares_sum(10))
    print(odd_squares_sum(30))
