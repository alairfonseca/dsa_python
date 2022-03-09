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

if __name__ == "__main__":
    a = [1, 3, 2, 6, -1, 4, 1, 8, 2]
    average_calc(a, 5)
    print("===========================")
    print("===========================")
    print("===========================")
    print("===========================")
    print("===========================")
