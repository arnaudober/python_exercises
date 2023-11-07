from copy import copy

menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 2.5
}


def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")


def check_resources(type):
    resources_needed = menu[type]['ingredients']
    resources_after_purchase = copy(resources)
    for ingredient in resources_needed:
        resources_after_purchase[ingredient] -= resources_needed[ingredient]
        if resources_after_purchase[ingredient] < 0:
            print(f"Sorry, there is not enough {ingredient}.")
            return None

    return resources_after_purchase


def ask_for_coins(coffee_cost):
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    total = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    if total < coffee_cost:
        print("Sorry, that's not enough money. Money refunded.")
        return None
    else:
        change = total - coffee_cost
        print(f"Here is ${change} in change.")
        return total


def refill():
    resources["water"] += 300
    resources["milk"] += 200
    resources["coffee"] += 100
    resources["money"] += 2.5


ask_again = True

while ask_again:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if user_choice == "off":
        ask_again = False
    elif user_choice == "refill":
        refill()
    elif user_choice == "report":
        print_report()
    elif user_choice == "espresso" or user_choice == "latte" or user_choice == "cappuccino":
        new_resources = check_resources(user_choice)
        if new_resources is None:
            continue
        user_change = ask_for_coins(menu[user_choice]["cost"])
        if user_change is None:
            continue
        else:
            resources = new_resources
            resources["money"] += menu[user_choice]["cost"]
            print(f"Here is your {user_choice} ☕️. Enjoy!")
    else:
        print("Invalid input.")
