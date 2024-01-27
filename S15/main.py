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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

### Code

def suff_res() :
    with MENU[input]["ingredients"] as drink :
        for ingredient in drink:
            if drink[ingredient] >= resources[ingredient] :
                 return False
    return True
                 
        


is_on = True
choice = input("What would you like? (espresso/latte/cappuccino):")

if choice == "off" :
    is_on = False
    sys.exit()
elif choice == "report" :
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
#        print(f"Money: ${profit}")
else :
     if suff_res() : print("good") 