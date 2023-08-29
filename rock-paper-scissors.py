import random

rock = '''
                _    
               | |   
 _ __ ___   ___| | __
| '__/ _ \ / __| |/ /
| | | (_) | (__|   < 
|_|  \___/ \___|_|\_\                     
'''

paper = '''
 _ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_|              
'''

scissors = '''
         _                        
         (_)                       
 ___  ___ _ ___ ___  ___  _ __ ___ 
/ __|/ __| / __/ __|/ _ \| '__/ __|
\__ \ (__| \__ \__ \ (_) | |  \__ \

|___/\___|_|___/___/\___/|_|  |___/
                                   
'''

ascii_art = [rock, paper, scissors]


def check_winner(user, computer):
    if user == 0 and computer == 2:
        return "You win!"
    elif user == 2 and computer == 0:
        return "You lose!"
    elif user == 2 and computer == 1:
        return "You win!"
    elif user == 1 and computer == 2:
        return "You lose!"
    elif user == 1 and computer == 0:
        return "You win!"
    elif user == 0 and computer == 1:
        return "You lose!"
    else:
        return "That's a draw!"


def is_input_valid(input_to_check):
    return input_to_check <= 2


user_action = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if is_input_valid(user_action) is False:
    print("You entered an incorrect number, you lose!")
    exit()

print(ascii_art[user_action])

computer_action = random.randint(0, 2)
print("Computer chose:")
print(ascii_art[computer_action])

print(check_winner(user_action, computer_action))
