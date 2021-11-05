
def report(self):
    for ingredient in self.resources:
        print(f"{ingredient}: {self.resources[ingredient]}")
    print(f"profit: {self.profit}")

def add_resources(self):
    ingredient = input("What do you want to add? water, milk or coffee ")
    amount = int(input("How much of it do you want to add? "))
    self.resources[ingredient] += amount

def check_resources(self, order):
    """Checks if the resources are enough to make the order """
    for ingredient in self.MENU[order]["ingredients"]:
        if self.resources[ingredient] < self.MENU[order]["ingredients"][ingredient]:
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

def check_transaction(self, order, total):
    """Checks if the total money is enough to buy the drink"""
    if total >= self.MENU[order]["cost"]:
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def transaction(self, order, total):
    """Does the transaction, adds the cost to profit and pays the extra to the user"""
    global profit
    self.profit += self.MENU[order]["cost"]

    if total > self.MENU[order]["cost"]:
        extra = round(total - self.MENU[order]["cost"], 2)
        print(f"Here is ${extra} dollars in change.")

def make_coffe(self, order):
    """makes the coffee and updates the resources"""
    for ingredient in self.MENU[order]["ingredients"]:
        self.resources[ingredient] -= self.MENU[order]["ingredients"][ingredient]
    
    print(f"Here is your {order} ☕. Enjoy!")
