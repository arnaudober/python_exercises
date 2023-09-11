alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(text, shift, direction):
    result_text = ""

    if direction == "decode":
        shift *= -1

    for char in text:
        index = alphabet.index(char)
        result_text += alphabet[(index + shift) % 26]

    print(f"The {direction}d text is {result_text}")


caesar(text, shift, direction)
