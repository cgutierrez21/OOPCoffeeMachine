from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import os

os.system("clear")

menu = Menu()
coffee_machine = CoffeeMaker()
latte = menu.menu[0].name
espresso = menu.menu[1].name
cappuccino = menu.menu[2].name
# print(menu.menu[0].name)

user_request = input("What would you like? (espresso/latte/cappuccino) ")

if user_request == "off":
    pass

elif user_request == "report":
    coffee_machine.report()

elif user_request == latte:
    # latte
    print(user_request)

elif user_request == espresso:
    # espresso
    print(user_request)

elif user_request == cappuccino:
    # cappuccino
    print(user_request)
