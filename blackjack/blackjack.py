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


def is_game_over(player_score, computer_score):
    if player_score == 21:
        print("You win :)")
        return True
    if computer_score > 21:
        print("Computer went over. You win :)")
        return True
    if computer_score == 21:
        print("You lose :(")
        return True
    if player_score > 21:
        print("You went over. You lose :(")
        return True

    return False


def play_next_move(player_cards, computer_cards):
    print(f"Your cards: {player_cards}, current score: {sum(player_cards)}")
    print(f"Computer's first card: {computer_cards[0]}")

    game_over = is_game_over(sum(player_cards), sum(computer_cards))
    if game_over:
        start_game()

    pick_another_card = input("Tap 'y' to get another card, type 'n' to pass: ")
    if pick_another_card == 'y':
        player_cards.append(draw_card())
    else:
        computer_cards.append(draw_card())

    play_next_move(player_cards, computer_cards)


def start_game():
    continue_playing = input("Do you want to play a game of blackjack? Type 'y' or 'n': ")

    while continue_playing == 'y':
        clear()
        print(logo)

        player_cards = [draw_card(), draw_card()]
        computer_cards = [draw_card(), draw_card()]

        play_next_move(player_cards, computer_cards)


start_game()
