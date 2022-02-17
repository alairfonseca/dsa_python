def sum_digits(n):
    print(n)
    if n == 0:
        return 0
    return int(n % 10) + sum_digits(n // 10)


if __name__ == "__main__":
    print(sum_digits(129))
