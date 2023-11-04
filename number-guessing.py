import random

logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
"""

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
mystery_number = random.randint(1, 100)


def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        return 10
    else:
        return 5


def check_guess(to_check, mystery, difficulty):
    if to_check == mystery:
        print(f"You got it! The answer was {mystery}.")
    elif to_check > mystery:
        print("Too high.\nGuess again.")
        print(f"You have {difficulty - 1} attempts remaining to guess the number.")
    elif to_check < mystery_number:
        print("Too low.")
        print("Guess again.")
        print(f"You have {difficulty - 1} attempts remaining to guess the number.")


def start_game():
    attempts = set_difficulty()
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))

    while guess != mystery_number and attempts > 0:
        check_guess(guess, mystery_number, attempts)
        attempts = attempts - 1

        if attempts == 0:
            print("You've run out of guesses, you lose.")
            break

        guess = int(input("Make a guess: "))


start_game()
