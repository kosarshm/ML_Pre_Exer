def rotation(alphabet, shift):

    shift %= len(alphabet)
    shifted_alphabet = alphabet[-shift:] + alphabet[:-shift]
    return shifted_alphabet


def cipher(text, shift):

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet_key = {}
    i = 0
    for letter in alphabet:
        alphabet_key.update({letter: i})
        i += 1
    shifted_alphabet = []
    shifted_alphabet = str(rotation(alphabet, shift))
    shifted_alphabet_key = {}
    i = 0
    for letter in shifted_alphabet:
        shifted_alphabet_key.update({i: letter})
        i += 1

    text_copy = text
    for item in text_copy:
        if item == " ":
            pass

        else:
            text_copy = text_copy.replace(item, shifted_alphabet_key.get(alphabet_key.get(item)))
    return text_copy


text, shift = str(input()), int(input())
print(cipher(text, shift))

