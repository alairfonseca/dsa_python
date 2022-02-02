def all_distinct(data):
    data.sort()

    for i in range(0, len(data) - 1):
        if data[i] == data[i+1]:
            return False
    return True


if __name__ == "__main__":
    print(all_distinct([1, 2, 3, 4, 5, 6]))
    print(all_distinct([5, 3, 1, 3, 4, 2]))
