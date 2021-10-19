from data import MENU, profit, resources

resources = {
    "water": 20,
    "milk": 20,
    "coffee": 10,
}


def check_resources(order):
    """ """
    for ingredient in MENU[order]["ingredients"]:
        if resources[ingredient] < MENU[order]["ingredients"][ingredient]:
            print(f"Sorry there is not enough {ingredient}")
            return False


def process_coins(order):

    quarters = int(input("How many quarter ? "))
    dimes = int(input(" How many dimes ? "))
    nickles = int(input(" How many nickles ? "))
    pennies = int(input(" How many pennies ? "))

    total = 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies
    return total


def check_transaction(order, total):

    if total >= MENU[order]["cost"]:
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def transaction(order, total):
    global profit
    profit += MENU[order]["cost"]

    if total > MENU[order]["cost"]:
        extra = total - MENU[order]["cost"]
        print(f"Here is ${extra} dollars in change.")


def make_coffe(order):
    for ingredient in MENU[order]["ingredients"]:
        resources[ingredient] -= MENU[order]["ingredients"]
    
    print("Here is your {order}. Enjoy!")



order = "espresso"
while order != "off":
    order = input("What would you like? (espresso/ latte/ cappuccino) ")

    if order == "report":
        print(resources)
        print(profit)

    
    elif order == "espresso" or order == "latte" or order == "cappuccino":
        if not check_resources(order):
            continue
        else:
            total = process_coins(order)
            if check_transaction(order, total):
                transaction(order, total)
                make_coffe(order)
