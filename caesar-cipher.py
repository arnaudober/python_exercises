alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift):
    cipher_text = ""

    for char in plain_text:
        index = alphabet.index(char)
        cipher_text += alphabet[(index + shift) % 26]

    print(f"The encoded text is {cipher_text}")

def decrypt(cipher_text, shift):
    plain_text = ""

    for char in cipher_text:
        index = alphabet.index(char)
        plain_text += alphabet[(index - shift) % 26]

    print(f"The decoded text is {plain_text}")

if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)
