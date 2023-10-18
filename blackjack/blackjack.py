import os
import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

possible_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def clear():
    os.system('clear')


def draw_card():
    return random.choice(possible_cards)


def compare_scores(player_score, computer_score):
    if player_score == computer_score:
        return "It's a draw :|"
    if computer_score == 0:
        return "Blackjack for the computer. You lose :("
    if player_score == 0:
        return "Blackjack! You win :)"
    if player_score > 21:
        return "You went over. You lose :("
    if computer_score > 21:
        return "Computer went over. You win :)"
    if player_score > computer_score:
        return "You win :)"
    else:
        return "You lose :("


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def new_game():
    print(logo)

    player_cards = [draw_card(), draw_card()]
    computer_cards = [draw_card(), draw_card()]
    is_game_over = False

    while not is_game_over:
        user_score = calculate_score(player_cards)
        computer_score = calculate_score(computer_cards)
        print(f"\tYour cards: {player_cards}, current score: {user_score}")
        print(f"\tComputer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            pick_another_card = input("Tap 'y' to get another card, type 'n' to pass: ")
            if pick_another_card == 'y':
                player_cards.append(draw_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(draw_card())
        computer_score = calculate_score(computer_cards)

    print(f"\tYour final cards: {player_cards}, final score: {user_score}")
    print(f"\tComputer's final cards: {computer_cards}, final score: {computer_score}")
    print(compare_scores(user_score, computer_score))


while input("Do you want to play a game of blackjack? Type 'y' or 'n': ") == 'y':
    clear()
    new_game()
