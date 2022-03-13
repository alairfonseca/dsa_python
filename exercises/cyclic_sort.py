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

if __name__ == "__main__":
    arrays = [[3, 1, 5, 4, 2], [2, 6, 4, 3, 1, 5], [1, 5, 6, 4, 3, 2]]
    for a in arrays:
        print(cyclic_sort(a))
    print("==========================")
    print("==========================")
    print("==========================")
    print("==========================")
