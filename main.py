from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffeemaker = CoffeeMaker()
moneymachine = MoneyMachine()

is_on = True

items = menu.get_items()

while is_on:
    choice = input(f"What woulḍ you like? ({items}): ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffeemaker.report()
        profit = moneymachine.report()
    else:
        drink = menu.find_drink(choice)
        if coffeemaker.is_resource_sufficient(drink) and moneymachine.make_payment(drink.cost):
           coffeemaker.make_coffee(drink)

