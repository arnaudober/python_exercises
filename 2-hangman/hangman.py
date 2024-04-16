from os import system
import random
from word_list import word_list
from hangman_art import logo, stages

# Select a random word
chosen_word = random.choice(word_list)

game_over = False
lives = 6

# Set up display with spaces
display = []
for letter in chosen_word:
    display.append("_")

print(logo)
print(f"chosen_word: {chosen_word}")

# Ask the user's guess
while not game_over:
    guess = input("Guess a letter: ").lower()

    system('clear')

    if guess in display:
        print(f"You've already guessed {guess}!")

    for index in range(len(chosen_word)):
        letter = chosen_word[index]
        if guess == letter:
            display[index] = letter

    if guess not in chosen_word:
        print(f"{guess} is not in the word. You lose a life.")

        lives = lives - 1
        if lives == 0:
            game_over = True
            print("Lost!")

    print(f"{' '.join(display)}")

    if "_" not in display:
        game_over = True
        print("Won!")

    print(stages[lives])
