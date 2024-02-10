from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def coffe_machine():
    my_menu = Menu()
    my_coffee_maker = CoffeeMaker()
    my_money_machine = MoneyMachine()
    is_on = True
    while is_on:
        options = my_menu.get_items()
        user_choice = input(f"Whate would you like ? {options} : ").lower()
        if user_choice == "report":
            my_coffee_maker.report()
            my_money_machine.report()
        elif user_choice == "off":
            is_on = False
        else:
            menu_item = my_menu.find_drink(user_choice)
            if menu_item:
                if my_coffee_maker.is_resource_sufficient(menu_item) and my_money_machine.make_payment(menu_item.cost):
                    my_coffee_maker.make_coffee(menu_item)

    

coffe_machine()