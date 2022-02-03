def can_use():
    a = int(input("enter a value"))
    b = int(input("enter b value"))
    c = int(input("enter c value"))

    can = (a + b == c) | (a == b - c) | (a * b == c)

    return can


if __name__ == "__main__":
    print(can_use())
