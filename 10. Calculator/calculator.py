# This is a simple Calculator pprogram.
# Level = Beginner

# Add
def add(first_num, secomd_num):
    return first_num + secomd_num

# Subtract
def subtract(first_num, secomd_num):
    return first_num - secomd_num

# multiply
def multiply(first_num, secomd_num):
    return first_num * secomd_num

# Divide
def divide(first_num, secomd_num):
    return first_num / secomd_num

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

from art import logo
def calculator():
    print(logo)
    continue_calculation = "y"
    print("Welcome to the Calculator:")
    first_num = float(input("Please enter the first number :\n"))
    operation = input(" +\n -\n *\n /\n Pick an operation : ")
    secomd_num = float(input("Please enter second number :\n"))

    function = operations[f"{operation}"]
    output = function(first_num, secomd_num)
    print(f"{first_num} {operation} {secomd_num} = {output}")

    while continue_calculation == "y":
        continue_calculation = input(f"Do you want to continue calculation with {output} as first number? or a new calculator? (y) to continue, (n) for a new calculator and (q) to quit : ")
        if continue_calculation == "y":

            first_num = function(first_num, secomd_num)
            operation = input(" +\n -\n *\n /\n Pick an operation : ")
            secomd_num = float(input("Please enter second number :\n"))
            function = operations[f"{operation}"]
            output = function(first_num, secomd_num)
            print(f"{first_num} {operation} {secomd_num} = {output}")
        
        elif continue_calculation == "n":
            calculator()

        else:
            print("Good Bye")
            

calculator()
