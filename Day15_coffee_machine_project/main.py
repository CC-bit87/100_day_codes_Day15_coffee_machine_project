from coffee_data import MENU
from coffee_data import resources


def espresso():
    espresso_ingredient = MENU['espresso'].get('ingredients')
    espresso_water_amount = espresso_ingredient['water']
    espresso_coffee_amount = espresso_ingredient['coffee']

    if water_resource < espresso_water_amount or coffee_resource < espresso_coffee_amount:
        print("Sorry there is not enough water.")
        return False

    else:
        new_water_resource = water_resource - espresso_water_amount
        resources['water'] = new_water_resource

        new_coffee_resource = coffee_resource - espresso_coffee_amount
        resources['coffee'] = new_coffee_resource
    # TODO 5. Process coins.
    print("Please insert coins")
    user_quarters = int(input("How many quarters?: ")) * 0.25
    user_dimes = int(input("How many dimes?: ")) * 0.10
    user_nickles = int(input("How many nickles?: ")) * 0.05
    user_pennies = int(input("How many pennies?: ")) * 0.01

    value_of_coins = user_quarters + user_dimes + user_nickles + user_pennies

    # TODO 6. Check transaction successful?

    if coffee_type == "espresso":
        espresso_cost = MENU['espresso'].get('cost')  # get() method. This method returns the value for colors if colors is in
        # the dictionary, else None, so that this method never raises a KeyError.
        if value_of_coins >= espresso_cost:
            transaction = round(value_of_coins - espresso_cost, 2)
            global Money
            Money += espresso_cost

            print(f"Your espresso costs ${espresso_cost}, your insert total coins ${value_of_coins}, Here is ${transaction} in change ")
            # TODO 7. Make Coffee.
            print("Here is your espresso ☕️. Enjoy!")
            return True

        else:
            print("Sorry that's not enough money. Money refunded.")
            return False


def latte():
    latte_ingredient = MENU['latte'].get('ingredients')
    latte_water_amount = latte_ingredient['water']
    latte_milk_amount = latte_ingredient['milk']
    latte_coffee_amount = latte_ingredient['coffee']

    if water_resource < latte_water_amount or milk_resource < latte_milk_amount or coffee_resource < latte_coffee_amount:
        print("Sorry there is not enough water.")
        return False

    else:
        new_water_resource = water_resource - latte_water_amount
        resources['water'] = new_water_resource

        new_milk_resource = milk_resource - latte_milk_amount
        resources['milk'] = new_milk_resource

        new_coffee_resource = coffee_resource - latte_coffee_amount
        resources['coffee'] = new_coffee_resource

    print("Please insert coins")
    user_quarters = int(input("How many quarters?: ")) * 0.25
    user_dimes = int(input("How many dimes?: ")) * 0.10
    user_nickles = int(input("How many nickles?: ")) * 0.05
    user_pennies = int(input("How many pennies?: ")) * 0.01

    value_of_coins = user_quarters + user_dimes + user_nickles + user_pennies

    if coffee_type == "latte":
        latte_cost = MENU['latte'].get('cost')

    if value_of_coins >= latte_cost:
        transaction = round(value_of_coins - latte_cost, 2)
        global Money
        Money += latte_cost

        print(
            f"Your latte costs ${latte_cost}, your insert total coins ${value_of_coins}, Here is ${transaction} in change ")
        print("Here is your Latte ☕️. Enjoy!")
        return True

    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def cappuccino():
    cappuccino_ingredient = MENU['cappuccino'].get('ingredients')
    cappuccino_water_amount = cappuccino_ingredient['water']
    cappuccino_milk_amount = cappuccino_ingredient['milk']
    cappuccino_coffee_amount = cappuccino_ingredient['coffee']

    if water_resource < cappuccino_water_amount or milk_resource < cappuccino_milk_amount or coffee_resource < cappuccino_coffee_amount:
        print("Sorry there is not enough water.")
        return False
    else:
        new_water_resource = water_resource - cappuccino_water_amount
        resources['water'] = new_water_resource

        new_milk_resource = milk_resource - cappuccino_milk_amount
        resources['milk'] = new_milk_resource

        new_coffee_resource = coffee_resource - cappuccino_coffee_amount
        resources['coffee'] = new_coffee_resource

    print("Please insert coins")
    user_quarters = int(input("How many quarters?: ")) * 0.25
    user_dimes = int(input("How many dimes?: ")) * 0.10
    user_nickles = int(input("How many nickles?: ")) * 0.05
    user_pennies = int(input("How many pennies?: ")) * 0.01

    value_of_coins = user_quarters + user_dimes + user_nickles + user_pennies

    if coffee_type == "cappuccino":
        cappuccino_cost = MENU['cappuccino'].get('cost')
        if value_of_coins >= cappuccino_cost:

            transaction = round(value_of_coins - cappuccino_cost, 2)
            global Money
            Money += cappuccino_cost

            print(f"Your cappuccino costs ${cappuccino_cost}, your insert total coins ${value_of_coins}, Here is ${transaction} in change ")
            print("Here is your cappuccino ☕️. Enjoy!")
            return True

        else:
            print("Sorry that's not enough money. Money refunded.")
            return False


Machine_on = True
Money = 0

while Machine_on:
    # TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
    coffee_type = input("What would you like? (espresso/latte/cappuccino): ")

    # TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt.
    if coffee_type == "off":
        print("Goodbye! 👋")
        Machine_on = False

    # TODO 3. Print report.
    water_resource = resources['water']
    milk_resource = resources['milk']
    coffee_resource = resources['coffee']

    if coffee_type == "report":
        print(f" Water {water_resource}ml \n Milk {milk_resource}ml \n Coffee {coffee_resource}g \n Money: ${Money}")

    # TODO 4. Check resources sufficient?
    if coffee_type == "espresso":
        espresso()
    elif coffee_type == "latte":
        latte()
    elif coffee_type == "cappuccino":
        cappuccino()
