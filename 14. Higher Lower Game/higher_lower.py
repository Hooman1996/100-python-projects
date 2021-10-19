# This is a game in which you will choose between two accounts that the program shows you that which one has more followers on instagram.
# each correct guess will add one score.
# Level = Beginner

from art import logo, vs 
from game_data import data
import random

def format_data(person):
    """ format the account data to seperate printable parts"""
    name = person["name"]
    description = person["description"]
    country = person["country"]
    return name, description, country


def higherLower():
    """ Plays the higher, lower game!"""

    score = 0
    result = True
    # print greeting art
    print(logo)

    # copy the data so we can play with it.
    ingame_data = data.copy()

    # randomly choosing the first account and removing it from data so it doesn't come up again
    person1 = random.choice(ingame_data)
    ingame_data.remove(person1)
        
    while result:
        
        # if all the accounts are removed then the game is finished.
        if len(ingame_data) < 1:
            print("Congrats You finished the whole game! You won")

        name, description, country = format_data(person1)

        print(f"Compare {name}, a {description}, from {country}.")
        print(vs)

        # randomly choosing the first account and removing it from data so it doesn't come up again
        person2 = random.choice(ingame_data)
        ingame_data.remove(person2)

        name, description, country = format_data(person2)

        print(f"Againts {name}, a {description}, from {country}.")

        # Check if player's guess is right
        a, b = person1["follower_count"] > person2["follower_count"], person2["follower_count"] > person1["follower_count"]
        guess = eval(input("Which one has more followers on instagram ? (a or b) ").lower())

        if guess: 
            score += 1
            # the account a now should be the last rounds account b
            person1 = person2
            print(f"You're right. Current score : {score}")

        
        else:
            print(f"Sorry thats wrong! Final score : {score}")
            go_dagain = input("go dagain? (y/n) ")
            if go_dagain == "y":
                higherLower()
            else:
                print("Goodbye")
                break
 
 
higherLower()