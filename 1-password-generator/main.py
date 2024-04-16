import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

letters_count = int(input("How many letters would you like in your password?\n"))
symbols_count = int(input("How many symbols would you like?\n"))
numbers_count = int(input("How many numbers would you like?\n"))

generated_characters = []


def pick_random_item_in_list(pick_list):
    item = random.choice(pick_list)
    generated_characters.append(item)


for i in range(letters_count):
    pick_random_item_in_list(letters)
for i in range(symbols_count):
    pick_random_item_in_list(symbols)
for i in range(numbers_count):
    pick_random_item_in_list(numbers)

random.shuffle(generated_characters)
generated_password = ''.join(generated_characters)
print(f'Here is your password: {generated_password}')
