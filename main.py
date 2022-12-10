from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import os, time

os.system("clear")

menu = Menu()
coffee_machine = CoffeeMaker()
money = MoneyMachine()

while True:
    user_request = input("What would you like? (espresso/latte/cappuccino) ")

    if user_request == "off":
        break

    elif user_request == "report":
        coffee_machine.report()
        money.report()

    elif menu.find_drink(user_request):
        drink = menu.find_drink(user_request)
        make_drink = coffee_machine.is_resource_sufficient(drink)
        if make_drink:
            enough_money = money.make_payment(drink.cost)
            if enough_money:
                coffee_machine.make_coffee(drink)
                
    time.sleep(3)
    os.system("clear")