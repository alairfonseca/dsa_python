import random


def shuffle(data):
    for i in range(0, len(data)):
        random_position = random.randint(0, len(data) - 1)

        tmp = data[random_position]
        data[random_position] = data[i]
        data[i] = tmp

    return data


if __name__ == "__main__":
    print(shuffle([1, 2, 3, 4, 5, 6, 7, 8, 9]))
