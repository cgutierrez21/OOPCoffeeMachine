from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import os

os.system("clear")

menu = Menu()
coffee_machine = CoffeeMaker()
money = MoneyMachine()
latte = menu.menu[0]
espresso = menu.menu[1]
cappuccino = menu.menu[2]
# print(menu.menu[0].name)

user_request = input("What would you like? (espresso/latte/cappuccino) ")
coffee_flavor = menu.find_drink(user_request)

if user_request == "off":
    pass

elif user_request == "report":
    coffee_machine.report()
    money.report()

elif menu.find_drink(user_request):
    drink = menu.find_drink(user_request)
    make_drink = coffee_machine.is_resource_sufficient(drink)
    if make_drink:
        enough_money = money.make_payment(drink.cost)
        coffee_machine.make_coffee(drink)


elif menu.find_drink(user_request) is None:
    print("Sorry either that item is not available or you have entered an incorrect input.")



