"""
Write a function to sort the objects in-place on their creation sequence number in O(n)
and without using any extra space. For simplicity, let’s assume we are passed an integer
array containing only the sequence numbers, though each number is actually an object.
"""
def cyclic_sort(nums):
    i = 0
    
    while i < len(nums):
        value = nums[i]

        if i + 1 != value:
            nums[i], nums[value - 1] = nums[value - 1], nums[i]
        else:
            i += 1
  
    return nums

# We are given an array containing n distinct numbers taken from the range 0 to n. Since the array has only n numbers out of the total n+1 numbers, find the missing number.
def find_missing_number(nums):
    highest = 0
    actual_sum = 0

    for i in nums:
        actual_sum += i
        if i > highest:
            highest = i
    
    no_missing_sum = sum(range(0, highest + 1))

    return no_missing_sum - actual_sum

# We are given an unsorted array containing numbers taken from the range 1 to ‘n’. The array can have duplicates, which means some numbers will be missing. Find all those missing numbers.
def find_missing_numbers(nums):
    missingNumbers = []
    i = 0

    while i < len(nums):
        value = nums[i]

        if value - 1 != i and nums[value - 1] != nums[i]:
            nums[i], nums[value - 1] = nums[value - 1], nums[i]
        else:
            i += 1

    for (i, v) in enumerate(nums):
        if v - 1 != i:
            missingNumbers.append(i + 1)

    return missingNumbers

"""
We are given an unsorted array containing ‘n+1’ numbers taken from the range 1 to ‘n’.
The array has only one duplicate but it can be repeated multiple times. Find that duplicate
number without using any extra space. You are, however, allowed to modify the input array.
"""
def find_duplicate(nums):
    i = 0

    while i < len(nums):
        value = nums[i]

        if value - 1 != i:
            if nums[value - 1] == nums[i]:
                return nums[i]
            else:
                nums[value - 1], nums[i] = nums[i], nums[value - 1]
        else:
            i += 1

    return -1

# We are given an unsorted array containing n numbers taken from the range 1 to n. The array has some numbers appearing twice, find all these duplicate numbers using constant space.
def find_all_duplicates(nums):
    duplicateNumbers = []
    i = 0

    while i < len(nums):
        value = nums[i]

        if value - 1 != i:
            if nums[value -1] == nums[i]:
                duplicateNumbers.append(value)
                i += 1
            else:
                nums[value - 1], nums[i] = nums[i], nums[value - 1]
        else:
            i += 1

    return duplicateNumbers

if __name__ == "__main__":
    arrays = [[3, 1, 5, 4, 2], [2, 6, 4, 3, 1, 5], [1, 5, 6, 4, 3, 2]]
    for a in arrays:
        print(cyclic_sort(a))
    
    print("==========================")
    arrays = [[4, 0, 3, 1], [8, 3, 5, 2, 4, 6, 0, 1]]
    for a in arrays:
        print(find_missing_number(a))

    print("==========================")
    arrays = [[2, 3, 1, 8, 2, 3, 5, 1], [2, 4, 1, 2], [2, 3, 2, 1]]
    for a in arrays:
        print(find_missing_numbers(a))

    print("==========================")
    arrays = [[1, 4, 4, 3, 2], [2, 1, 3, 3, 5, 4], [2, 4, 1, 4, 4]]
    for a in arrays:
        print(find_duplicate(a))

    print("==========================")
    arrays = [[3, 4, 4, 5, 5], [5, 4, 7, 2, 3, 5, 3]]
    for a in arrays:
        print(find_all_duplicates(a))
