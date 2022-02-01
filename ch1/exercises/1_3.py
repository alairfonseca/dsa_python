def minmax(data):
    smallest = data[0]
    largest = data[0]

    for i in data:
        if i < smallest:
            smallest = i
        if i > largest:
            largest = i

    return (smallest, largest)


if __name__ == "__main__":
    print(minmax([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    print(minmax([31, 29, 103, 45, 43, 102, 21, 20]))
