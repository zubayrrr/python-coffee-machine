MENU = {
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

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_resources(ingredients):
    """Returns True when resources are available, False when not available."""
    for i in ingredients:
        if ingredients[i] >= resources[i]:
            print(f"Sorry there is not enough {i}")
            return False
    return True


def check_coins():
    """returns total amount from coins inserted"""
    print("Please insert coins.")
    total = int(input("How many quarters: ")) * 0.25
    total += int(input("How many dimes: ")) * 0.1
    total += int(input("How many nickles: ")) * 0.05
    total += int(input("How many pennies: ")) * 0.01
    return total


def transaction(payment, cost):
    """Return True when payment is accepted, False if payment is insufficient."""
    if payment >= cost:
        change = round(payment - cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += cost
        return True
    else:
        print("Sorry, that is not enough money, money refunded.")
        return False


def coffee(drink, ingredients):
    """Deduct ingredients from resources"""
    for i in ingredients:
        resources[i] -= ingredients[i]
    print(f"Here is your {drink} ☕, Enjoy!")

power = True


while power:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        print("Powering off Coffee Machine...")
        power = False
    elif choice == "report":
        print(
            f"Water: {resources['water']}\nMilk: {resources['milk']} \nCoffee: {resources['coffee']} \nMoney: ${profit}")
    else:
        drink = MENU[choice]
        if check_resources(drink['ingredients']):
            payment = check_coins()
            if transaction(payment, drink['cost']):
                coffee(choice, drink['ingredients'])

# TODO: 1. Print report of all coffee machine resources
