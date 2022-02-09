# factorial function
def factorial(n):
    if n == 0:
        return 1

    return n * factorial(n - 1)


if __name__ == "__main__":
    print(factorial(6))
    print(factorial(5))
