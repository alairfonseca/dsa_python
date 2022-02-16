class CaesarCipher:
    def __init__(self, shift):
        encoder = [None] * 26
        decoder = [None] * 26

        for i in range(26):
            encoder[i] = chr((i + shift) % 26 + ord('A'))
            decoder[i] = chr((i - shift) % 26 + ord('A'))

        self._forward = "".join(encoder)
        self._backward = "".join(decoder)

    def encrypt(self, message):
        return self._transform(message, self._forward)

    def decrypt(self, message):
        return self._transform(message, self._backward)

    def _transform(self, original, code):
        msg = list(original.upper())

        for i in range(len(msg)):
            if msg[i].isalpha():
                subs_index = ord(msg[i]) - ord('A')
                msg[i] = code[subs_index]

        return "".join(msg)


if __name__ == "__main__":
    cipher = CaesarCipher(3)
    msg = "the eagle is in play; meet at joe's."
    msg2 = "o rato roeu a roupa do rei de roma"
    msgs = [msg, msg2]

    for i in msgs:
        coded = cipher.encrypt(i)
        print("coded:", coded)
        decoded = cipher.decrypt(coded)
        print("decoded:", decoded)
