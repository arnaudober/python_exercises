from coffee_maker import CoffeeMaker
from menu import Menu
from money_machine import MoneyMachine

menu = Menu()
moneyMachine = MoneyMachine()
coffeeMaker = CoffeeMaker()

ask_again = True

while ask_again:
    user_choice = input(f"What would you like? ({menu.get_items()}): ")
    if user_choice == "off":
        ask_again = False
    elif user_choice == "report":
        coffeeMaker.report()
        moneyMachine.report()
    elif user_choice == "espresso" or user_choice == "latte" or user_choice == "cappuccino":
        drink = menu.find_drink(user_choice)
        if coffeeMaker.is_resource_sufficient(drink) and moneyMachine.make_payment(drink.cost):
            coffeeMaker.make_coffee(drink)
    else:
        print("Invalid input.")
