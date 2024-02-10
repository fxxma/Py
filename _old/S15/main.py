import sys

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

### Code

def suff_res() :
    drink = MENU[choice]["ingredients"]
    for ingredient in drink:
        if drink[ingredient] >= resources[ingredient] :
            print(f"Sorry there is not enough {ingredient}.")
            return False

    return True

def coin_process() :
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def succ_trans(user) :
    drink_cost = MENU[choice]["cost"]
    if user < drink_cost :
        print("Sorry that's not enough money. Money refunded.")
        return False
    else :
        global profit
        profit += drink_cost
        change = user - drink_cost
        if change > 0 :
            print(f"Here is ${change} dollars in change.")
        return True

def make_coffee() :
    drink = MENU[choice]["ingredients"]
    for ingredient in drink :
        resources[ingredient] -= drink[ingredient]
    print(f"Here is your {choice}.Enjoy!")
    
is_on = True
while is_on :
    choice = input("What would you like? (espresso/latte/cappuccino):")
    if choice == "off" :
        is_on = False
    elif choice == "report" :
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${profit}")
    else :
        if suff_res():
            amt = coin_process()
            if succ_trans(amt) :
                make_coffee()