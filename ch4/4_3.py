# Good recursive fibonacci
def fibonacci(n):
    if n <= 1:
        return (n, 0)
    else:
        (a, b) = fibonacci(n - 1)
        print(a+b)
        return (a + b, a)


if __name__ == "__main__":
    fibonacci(10)
