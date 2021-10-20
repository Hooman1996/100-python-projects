from data import MENU, profit, resources

def check_resources(order):
    """Checks if the resources are enough to make the order """
    for ingredient in MENU[order]["ingredients"]:
        if resources[ingredient] < MENU[order]["ingredients"][ingredient]:
            print(f"Sorry there is not enough {ingredient}")
            return False
        else:
             return True


def process_coins(order):
    """Returns the total calculated from coins inserted"""
    print("Please insert coins ")
    quarters = int(input("How many quarter ? "))
    dimes = int(input("How many dimes ? "))
    nickles = int(input("How many nickles ? "))
    pennies = int(input("How many pennies ? "))

    total = 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies
    return total


def check_transaction(order, total):
    """Checks if the total money is enough to buy the drink"""
    if total >= MENU[order]["cost"]:
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def transaction(order, total):
    """Does the transaction, adds the cost to profit and pays the extra to the user"""
    global profit
    profit += MENU[order]["cost"]

    if total > MENU[order]["cost"]:
        extra = round(total - MENU[order]["cost"], 2)
        print(f"Here is ${extra} dollars in change.")


def make_coffe(order):
    """makes the coffee and updates the resources"""
    for ingredient in MENU[order]["ingredients"]:
        resources[ingredient] -= MENU[order]["ingredients"][ingredient]
    
    print(f"Here is your {order} ☕. Enjoy!")

def add_resources():
    ingredient = input("What do you want to add? water, milk or coffee ")
    amount = int(input("How much of it do you want to add? "))
    resources[ingredient] += amount


def coffee_machine():
    order = ""
    while order != "off":
        order = input("What would you like? (espresso/ latte/ cappuccino) ")

        if order == "report":
            for ingredient in resources:
                print(f"{ingredient}: {resources[ingredient]}")
            print(f"profit: {profit}")    
        
        elif order == "fill machine":
            add_resources()
        
        elif order == "espresso" or order == "latte" or order == "cappuccino":
            if not check_resources(order):
                continue
            else:
                total = process_coins(order)
                if check_transaction(order, total):
                    transaction(order, total)
                    make_coffe(order)
    else: 
        print("Good Bye")

coffee_machine()
