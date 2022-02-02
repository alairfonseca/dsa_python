def find_odd_pairs(data):
    odd_counter = 0
 
    for i in data:
        if i % 2 != 0:
            odd_counter += 1

    return odd_counter >= 2

if __name__ == "__main__":
    sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(find_odd_pairs(sequence))
    print(find_odd_pairs([2, 4, 6, 7]))
