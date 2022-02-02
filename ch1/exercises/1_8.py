s = "test string"
n = len(s)

print(n)
print(s[-n])

for k in range(-n, 0):
    print(s[k])

for j in range(0, n):
    print(s[j - n])
