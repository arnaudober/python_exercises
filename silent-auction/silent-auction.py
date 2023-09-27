import os

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''


def clear():
    os.system('clear')


def find_highest_bid(auctioneers):
    highest_bid_name = ""
    highest_bid = 0

    for key in auctioneers:
        current_bid = auctioneers[key]
        if current_bid > highest_bid:
            highest_bid = current_bid
            highest_bid_name = key

    return highest_bid_name


def game():
    print(logo)

    auctioneers = {}

    continue_biding = True
    while continue_biding:

        name = input("What's your name?: ")
        bid = input("What's your bid?: $")

        auctioneers[name] = int(bid)
        continue_biding = input("Is there other auctioneers?: ") == "Yes"
        clear()

    winner = find_highest_bid(auctioneers)
    print(f"{winner} wins the bid!")


game()
