alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift):
    cipher_text = ""

    for char in plain_text:
        index = alphabet.index(char)
        cipher_text += alphabet[(index + shift) % 26]

    return cipher_text

cipher_text = encrypt(text, shift)
print(cipher_text) # ekxknkccvkqp