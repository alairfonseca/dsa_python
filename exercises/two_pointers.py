# Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target.
def pair_with_targetsum(arr, target_sum):
    a = 0
    b = len(arr) - 1

    while a < b:
        res = arr[a] + arr[b]

        if res == target_sum:
            print([a, b])
            return
        elif res > target_sum:
            b -= 1
        elif res < target_sum:
            a += 1

    print([-1, -1])

# Given an array of sorted numbers, remove all duplicates from it. You should not use any extra space; after removing the duplicates in-place return the length of the subarray that has no duplicate in it.
def remove_duplicates(arr):
    i = 1
    duplicates = 0

    while i < len(arr):
        if arr[i - 1] == arr[i]:
            duplicates += 1
        i += 1

    return len(arr) - duplicates

if __name__ == "__main__":
    arrays = [[1, 2, 3, 4, 6], [2, 5, 9, 11]]
    ts = [6, 11]
    for (i, a) in enumerate(arrays):
        pair_with_targetsum(a, ts[i])
    print("===========================")
    arrays = [[2, 3, 3, 3, 6, 9, 9], [2, 2, 2, 11], [1, 2, 3, 4, 5, 6]]
    for a in arrays:
        print(remove_duplicates(a))

    print("===========================")
    print("===========================")
    print("===========================")
    print("===========================")
    print("===========================")
    print("===========================")
    print("===========================")
    print("===========================")
    print("===========================")
    print("===========================")
    print("===========================")
    print("===========================")
    print("===========================")
    print("===========================")
    print("===========================")
    print("===========================")
    print("===========================")
    print("===========================")
    print("===========================")
    print("===========================")
    print("===========================")
