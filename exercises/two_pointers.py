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

if __name__ == "__main__":
    arrays = [[1, 2, 3, 4, 6], [2, 5, 9, 11]]
    ts = [6, 11]
    for (i, a) in enumerate(arrays):
        pair_with_targetsum(a, ts[i])
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
    print("===========================")
