arr = [
        [11, 15, 10, 6],
        [10, 14, 11, 5],
        [12, 17, 12, 8],
        [15, 18, 14, 9]
      ]

for i in arr:
    for j in i:
        print(j, end = " ")
    print("")
    

print("\n\n\n\n")

arr.remove(arr[0])
arr.pop()

for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j], end = " ")
    print("")



