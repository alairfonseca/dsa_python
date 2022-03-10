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

# Given a sorted array, create a new array containing squares of all the numbers of the input array in the sorted order.
def make_squares(arr):
    result = [0] * len(arr)
    a = 0
    b = len(arr) - 1
    current_insert_index = b

    while a < b:
        sqra = abs(arr[a] ** 2)
        sqrb = abs(arr[b] ** 2)

        if sqra > sqrb:
            result[current_insert_index] = sqra
            result[current_insert_index - 1] = sqrb
        else:
            result[current_insert_index] = sqrb
            result[current_insert_index - 1] = sqra

        current_insert_index -= 2

        b -= 1
        a += 1

    return result

# Given an array of unsorted numbers, find all unique triplets in it that add up to zero.
def search_triplets(arr):
    result = []
    arr.sort()

    for i in range(len(arr)):
        if arr[i] > 0:
            continue
        search_pair(arr, arr[i], i + 1, result)

    return result

def search_pair(arr, target, a, triplets):
    b = len(arr) - 1

    while a < b:
        if arr[a] + arr[b] + target == 0:
            triplets.append([target, arr[a], arr[b]])
            a += 1
            b -= 1
        elif arr[a] + arr[b] + target < 0:
            a += 1
        else:
            b -= 1

# Given an array of unsorted numbers and a target number, find a triplet in the array whose sum is as close to the target number as possible, return the sum of the triplet. If there are more than one such triplet, return the sum of the triplet with the smallest sum.
def triplet_sum_close_to_target(arr, target_sum):
    result = 0
    triplets = []
    arr.sort()

    for i in range(len(arr)):
        if arr[i] > target_sum:
            continue
        search_pairs(arr, arr[i], target_sum, i + 1, triplets)
    
    for a in triplets:
        result = max(result, sum(a))
    
    return result

def search_pairs(arr, first_element, target, a, triplets):
    b = len(arr) - 1

    while a < b:
        if first_element + arr[a] + arr[b] <= target:
            triplets.append([first_element, arr[a], arr[b]])
            a += 1
        elif first_element + arr[a] + arr[b] > target:
            b -= 1

# Given an array arr of unsorted numbers and a target sum, count all triplets in it such that arr[i] + arr[j] + arr[k] < target where i, j, and k are three different indices. Write a function to return the count of such triplets.
def triplet_with_smaller_sum(arr, target):
    result = 0
    arr.sort()
    
    for i in range(len(arr)):
        result += search_pairs2(arr, target - arr[i], i + 1)
    
    return result

def search_pairs2(arr, target, a):
    b = len(arr) - 1
    count = 0

    while a < b:
        if arr[a] + arr[b] < target:
            count += b - a
            a += 1
        else:
            b -= 1
    
    return count

# Given an array with positive numbers and a positive target number, find all of its contiguous subarrays whose product is less than the target number.
def find_subarrays(arr, target):
    result = []
    a = 0
    b = 1

    product = 1

    while a <= b and b < len(arr):
        for i in range(a, b+1):
            product *= arr[i]

        if product < target:
            result.append(arr[a:b+1])
            b += 1
        else:
            result.append([arr[a]])
            product = 1
            a += 1
    
    return result

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
    arrays = [[-2, -1, 0, 2, 3], [-3, -1, 0, 1, 2]]
    for a in arrays:
        print(make_squares(a))
    
    print("===========================")
    arrays = [[-3, 0, 1, 2, -1, 1, -2], [-5, 2, -1, -2, 3]]
    for a in arrays:
        print(search_triplets(a))

    print("===========================")
    arrays = [[-2, 0, 1, 2], [-3, -1, 1, 2], [1, 0, 1, 1]]
    ts = [2, 1, 100]
    for (i, a) in enumerate(arrays):
        print(triplet_sum_close_to_target(a, ts[i]))
    
    print("===========================")
    arrays = [[-1, 0, 2, 3], [-1, 4, 2, 1, 3]]
    ts = [3, 5]
    for (i, a) in enumerate(arrays):
        print(triplet_with_smaller_sum(a, ts[i]))
    
    print("===========================")
    arrays = [[2, 5, 3, 10], [8, 2, 6, 5]]
    ts = [30, 50]
    for (i, a) in enumerate(arrays):
        print(find_subarrays(a, ts[i]))
    print("===========================")
    print("===========================")
    print("===========================")
    print("===========================")
    print("===========================")
    print("===========================")
    print("===========================")
    print("===========================")
    print("===========================")
