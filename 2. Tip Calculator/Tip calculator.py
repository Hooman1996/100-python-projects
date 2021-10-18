# This program helps you to calcute how much should every person pay in a resturant based on:
# the precentage of the tip you want to pay
# how many people are there at your table
# and the total bill

# Level = Beginner

# Greeting
print("Welcome to the tip calculator. ")

# Getting the total bill from the user and casting it to float type
bill = float(input(" What was the total bill? $"))

# Getting the tip precentage from the user and casting it to int type
tip = int(input("What precentage of tip would you like to give?  10, 12, or 15? "))

# Getting the number of people that share the bill from the user and casting it to int type
people = int(input(" How many people to split the bill? "))

# Calculating the share each person should pay taking into account the total bill and the tip
total = bill * (1 + tip/100)
each_share = round(total/ people, 2)
final_amount = "{:.2f}".format(each_share)
print(f"Each person should pay : {final_amount} $")

# Note that each time we call the input function, there is a chance that user inputs something not proper as the input
# such as inputing a word instead of a number for the total bill amount.
# we can use ways like using try/except's to prevent the code from outputting an error
# but i didn't do that so the simplicity of the code stays the same.