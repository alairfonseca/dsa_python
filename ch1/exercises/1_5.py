def squares_sum(n):
    return sum([i ** 2 for i in range(0, n)])


if __name__ == "__main__":
    print(squares_sum(5))
    print(squares_sum(10))
    print(squares_sum(30))
