# Level = Beginner

import random
from art import logo

def number_guessing():
    # Greeting 
    print(logo)
    print("Welcome to the Number Guessing Ggame !")
    print("I'm thinking of a number between 0 and 100.")

    difficulty = input("Choose a difficulty. Type 'easy' of 'hard : ")
    if difficulty == "easy":
        chances = 10
    elif difficulty == "hard":
        chances = 5

    print(f"You have {chances} chances")
    number =random.randint(1, 100) 

    for i in range(1, chances+1):
        
        guess = int(input("Make a guess :  "))
        if guess == number:
            print("You Got it !!")
            return None
        elif guess > number:
            print(" Too high")
            print(f"You have {chances - i} chances left ")
            
        elif guess < number:
            print(" Too low")
            print(f"You have {chances - i} chances left ")

        if i != chances:
            print("Go again")

    print("You've ran out of guesses, You Lost !!")


number_guessing()
