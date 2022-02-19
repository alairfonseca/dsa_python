# determine if all elements in a list are uniq


def is_uniq(sequence):
    visited_elements = []

    for i in sequence:
        if not i in visited_elements:
            visited_elements.append(i)
        else:
            return False
    
    return True


print(is_uniq([1, 2, 3, 4, 5, 6]))
print(is_uniq([1, 2, 3, 4, 5, 5]))
