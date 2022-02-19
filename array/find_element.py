# check if an array contains a number


def find_element(sequence, target):
    for i in sequence:
        if i == target:
            return i
    return "element not found"


print(find_element([i + 1 for i in range(0, 50)], 34))
print(find_element([1, 2, 3, 4], 5))
