def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


def better_fib(n):
    if n <= 1:
        return (n, 0)
    (a, b) = better_fib(n - 1)
    
    print(a, b)
    print(a + b)

    return (a + b, a)


if __name__ == "__main__":
    print(fib(5))
    print(fib(10))
    print("====================")
    better_fib(5)
