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
    print("==========================")
