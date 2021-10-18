# This is a secret or silent auction in which be inputin every bidders bid, the program will tell who won the auction.
# Level = Beginner

from art import logo
import os
clear = lambda: os.system('cls')  # On Windows System

print(logo)
bidders = []
print("Welcome to the secret auction program.")
more_bidders = "y"
while more_bidders == "y":
    name = input("What is your name?\n")
    bid = int(input("How much do you want to bid? $ "))
    bidder = {"name": f"{name}", "bid": bid}
    bidders.append(bidder)
    more_bidders = input("Are there any more bidders?(y/n) : \n")
    clear()


winner = bidders[0]
for bidder in bidders:
    if bidder["bid"] > winner["bid"]:
        winner = bidder

bid_amount = winner["bid"]
winner_name = winner["name"]
print(f"The winner is {winner_name} with the bid amount of {bid_amount}")
