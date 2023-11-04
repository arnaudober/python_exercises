import os
import random

from art import logo, vs
from game_data import data


def clear():
    os.system('clear')


score = 0
continue_game = True

while continue_game:
    print(logo)

    account1 = random.choice(data)
    print(f"Compare A: {account1['name']}, a {account1['description']}, from {account1['country']}.")

    print(vs)

    # To avoid the same account being chosen twice
    account2 = account1
    while account2 == account1:
        account2 = random.choice(data)
    print(f"Against B: {account2['name']}, a {account2['description']}, from {account2['country']}.")

    first_is_higher = account1['follower_count'] > account2['follower_count']
    answer = input("Who has more followers? Type 'A' or 'B': ")
    if (answer == "A" and first_is_higher) or answer == "B" and not first_is_higher:
        score = score + 1
        print(f"You're right! Current score: {score}")
        clear()
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        continue_game = False

