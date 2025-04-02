from menu import Menu , MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

"""create the objects using imported classes"""

menu = Menu()
coffee_making = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True 

while is_on:
    option = menu.get_items()
    user_choice = input(f"What would you like? ({option})").lower()
    if user_choice == "off":
        is_on = False 
    elif user_choice == "report":
        coffee_making.report()
        money_machine.report()
    else:
        #adding a try_execpt block in case users input is incorrect 
        try:
            drink = menu.find_drink(user_choice)
            if drink is None:
                raise ValueError("Invalid drink selected.")
            #check to see id the resources are sufficient and they are able tp make a payment 
            if coffee_making.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_making.make_coffee(drink)

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Somthing when wrong: {e}")