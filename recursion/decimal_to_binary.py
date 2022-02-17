def dec_to_bin(n):
    if n == 0:
        return 0
    return dec_to_bin(n // 2) * 10 + (n % 2)


if __name__ == "__main__":
    print(dec_to_bin(13))
    print(dec_to_bin(10))
