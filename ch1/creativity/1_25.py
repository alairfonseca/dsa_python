import re

def remove_punctuation(sentence):
    response = re.sub(r'[^a-zA-Z0-9\s]', '', sentence)

    return response


if __name__ == "__main__":
    s = "Let's try, Mike."
    print(remove_punctuation(s))
