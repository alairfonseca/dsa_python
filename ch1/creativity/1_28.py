def norm(vector, p = 2):
    sum = 0
    for i in vector:
        sum += i**p
    
    return sum ** (1/p)


if __name__ == "__main__":
    print(norm([1, 2, 3, 4]))
