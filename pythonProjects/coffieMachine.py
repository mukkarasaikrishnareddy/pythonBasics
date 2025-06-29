MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18
        },
        "cost": 1.5
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "coffee": 24,
            "milk": 150
        },
        "cost": 2.5
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "coffee": 24,
            "milk": 100
        },
        "cost": 3.0
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "coffee": 24,
            "milk": 150
        },
        "cost": 2.5
    }
}
profit  = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}
def check_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True
def process_coins():
    """Returns the total calculated from coins inserted by the user."""
    print("please insert coins:")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickels?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total
def is_transaction_successful(money_received, drink_cost):
    """Returns True if the transaction is successful, False otherwise."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False
    
is_on = True
while is_on:
    choice = input("what would you like (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Profit: ${profit}")
    else:
            drink = MENU[choice]
            if check_resources(drink["ingredients"]):
                process = process_coins()
                if is_transaction_successful(process, drink["cost"]):
                    profit += drink["cost"]
                    for item in drink["ingredients"]:
                        resources[item] -= drink["ingredients"][item]
                    print(f"Here is your {choice} ☕️. Enjoy!")
                    
                    