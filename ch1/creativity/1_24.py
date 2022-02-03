def count_vowels(text):
    vowels = "aeiou"
    result = 0

    for ch in text.lower():
        if ch in vowels:
            result += 1

    return result


if __name__ == "__main__":
    print(count_vowels("Alair"))
    print(count_vowels("aeiou"))
    print(count_vowels("xyz"))
