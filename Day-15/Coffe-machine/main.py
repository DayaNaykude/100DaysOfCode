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
# print report 
def print_report(water,milk,coffe, money):
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffe}g")
    print(f"Money: ${money}")


# check resources sufficeint for choosed drink
def is_resources_sufficient(drink_flavour, remaning_water, remaning_milk, remaning_coffee):
    choosed_menu_ingredients = MENU[drink_flavour]["ingredients"]
    print(choosed_menu_ingredients)
    if choosed_menu_ingredients["water"] > remaning_water:
        print("Sorry there is not enough water.")
        return False
    if drink_flavour != "espresso" and choosed_menu_ingredients["milk"] > remaning_milk :
        print("Sorry there is not enough milk.")
        return False
    if choosed_menu_ingredients["coffee"] > remaning_coffee:
        print("Sorry there is not enough coffee")
        return False
    return True

# process coins
def process_coins():
    quarters = int(input("Insert quarters: "))
    dimes = int(input("Insert dimes: "))
    nickles = int(input("Insert nickles: "))
    pennies = int(input("Insert pennies: "))

    return (0.25 * quarters) + (0.1 * dimes) + (0.05 * nickles) + (0.01 * pennies)

# chceck transcation successfull
def is_successful_transaction(drink_flavour, coins_inserted):
    drink_cost = MENU[drink_flavour]["cost"]
    if drink_cost > coins_inserted:
        print("Sorry that's not enough money. Money refunded")
        return False
    elif drink_cost == coins_inserted:
        return True
    else:
        offer_change = round((coins_inserted - drink_cost),2)
        print(f"Here is change:$ {offer_change}")
        return True

def coffe_machine(resources):
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    money = 0

    should_continue_serve = True
    while should_continue_serve:
        user_input = input("Whate would you like ? (espresso/latte/cappuccino):").lower()
        if user_input == "report":
            print_report(water, milk, coffee, money)
        elif user_input == "off":
            should_continue_serve = False
            return
        else:
            if is_resources_sufficient(user_input, water, milk, coffee):
                print(f"cost of coffe : {MENU[user_input]['cost']}")
                coin_inserted = process_coins()
                if is_successful_transaction(user_input, coin_inserted):
                    # update resources
                    choosed_menu = MENU[user_input]["ingredients"]
                    water = water - choosed_menu["water"]
                    if user_input != "espresso":
                        milk = milk - choosed_menu["milk"]
                    coffee = coffee - choosed_menu["coffee"]

                    # update profit
                    money = money + coin_inserted
                    print(f"Here is your {user_input}. Enjoy!")

coffe_machine(resources)
