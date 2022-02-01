
def odd_squares_sum(n):
    return sum([i ** 2 for i in range(0, n) if i % 2 == 0])


if __name__ == "__main__":
    print(odd_squares_sum(5))
    print(odd_squares_sum(10))
    print(odd_squares_sum(30))
