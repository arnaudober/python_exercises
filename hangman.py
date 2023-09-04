import random

# Select a random word
word_list = ['ardvark', 'baboon', 'camel']
chosen_word = random.choice(word_list)

# Ask the user's guess
guess = input("Guess a letter: ").lower()
for letter in chosen_word:
    if guess == letter:
        print('Right')
    else:
        print("Wrong")
