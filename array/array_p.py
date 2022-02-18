from array import *

# 1
arr = array('i', [1, 2, 3, 4, 5])

for i in arr:
    print(i)
    # O(n)

# 2
print(arr[2])
    # O(1)

# 3
arr.append(2) # O(1)
print(arr)

# 4
arr.insert(2, 6) # O(n)
print(arr)

# 5
arr.extend([6, 7, 8, 9]) # O(n)
print(arr)

# 6
arr.fromlist([1, 2, 3])
print(arr)

# 7
arr.remove(2) # O(n)
print(arr)

# 8
arr.pop() # O(1)
print(arr)

# 9
print(arr[1]) # O(1)

# 10
arr.reverse() # O(n)
print(arr)

# 11
print(arr.buffer_info())

# 12
print(arr.count(2)) # O(n)

# 14
arr.tolist() # O(n)

# 16
print(arr[1:5])
