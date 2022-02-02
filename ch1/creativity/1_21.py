text = []
eof = False

while not eof:
    try:
        line = input(
            "Enter text lines\nEnter ctrl-D to indicate the end of text\n"
        )
        text.append(line)
    except EOFError:
        eof = True
        for i in range(len(text) - 1, -1, -1):
            print(text[i])
