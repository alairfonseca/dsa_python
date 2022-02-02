import random


def get_random(data):
    return data[random.randrange(0, 9-1)]


if __name__ == "__main__":
    sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    print(get_random(sequence))
