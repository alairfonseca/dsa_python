import math

# Given an array, find the average of all subarrays of ‘K’ contiguous elements in it.
def average_calc(sequence, k):
    result = []
    window_start = 0

    window_sum = 0
    
    for window_end in range(len(sequence)):
        window_sum += sequence[window_end]

        if window_end >= k - 1:
            result.append(window_sum / k)
            window_sum -= sequence[window_start]
            window_start += 1
       
    print(result)

# Given an array of positive numbers and a positive number ‘k,’ find the maximum sum of any contiguous subarray of size ‘k’.
def maximum_sum(sequence, k):
    result = 0
    window_start = 0
    window_sum = 0

    for window_end in range(len(sequence)):
        window_sum += sequence[window_end]

        if window_end >= k - 1:
            result = max(result, window_sum)
            window_sum -= sequence[window_start]
            window_start += 1
    
    print(result)

# Given an array of positive numbers and a positive number ‘S,’ find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. Return 0 if no such subarray exists.
def smallest_subarray_greater_than_s(sequence, s):
    result = math.inf
    window_start = 0
    window_sum = 0

    for window_end in range(len(sequence)):
        window_sum += sequence[window_end]

        while window_sum >= s:
            result = min(result, (window_end - window_start) + 1)
            window_sum -= sequence[window_start]
            window_start += 1
        
    if (result == math.inf):
        print(0)
        return
    print(result)


if __name__ == "__main__":
    a = [1, 3, 2, 6, -1, 4, 1, 8, 2]
    average_calc(a, 5)
    print("===========================")
    a = [2, 3, 4, 1, 5]
    maximum_sum(a, 2)
    print("===========================")
    a = [2, 1, 5, 2, 3, 2]
    smallest_subarray_greater_than_s(a, 7)
    a = [2, 1, 5, 2, 8]
    smallest_subarray_greater_than_s(a, 7)
    a = [3, 4, 1, 1, 6]
    smallest_subarray_greater_than_s(a, 8)
    print("===========================")
    print("===========================")
    print("===========================")
