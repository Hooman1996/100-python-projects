from coffe_machine import *
from data import MENU, profit, resources

class MenuItem():
    def __init__(self, name, cost, ingredients):
        self.name = name
        self.cost = cost
        self.ingredients = ingredients
        self.Menu = MENU

class CoffeMachine():
    def __init__(self, resources, profit, MENU):
        self.resources = resources
        self.MENU = MENU
        self.profit = profit

    def report(self):
        report(self)

    def fill_machine(self):
        add_resources(self)
    
    def make_coffe(self, order):
        if not check_resources(self, order):
                return None
        else:
            total = process_coins(order)
            if check_transaction(self, order, total):
                transaction(self, order, total)
                make_coffe(self, order)

    def start(self):
        order = ""
        while order != "off":
            order = input("What would you like? (espresso/ latte/ cappuccino) ")

            if order == "report":
                self.report()    
            
            elif order == "fill machine":
                self.fill_machine()
            
            elif order == "espresso" or order == "latte" or order == "cappuccino":
                self.make_coffe(order)
                
        else: 
            print("Good Bye")

machine = CoffeMachine(resources, profit, MENU)
machine.start()
