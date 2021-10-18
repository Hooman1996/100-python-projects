# this is the code implementation of the rock, paper, scissors game.
# in each round you choose between your three options 
# and the game will tell you if you win or lose depending on the random choise of the computer.

# Level = Beginner

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

def rock_paper_scissor():

    import random
    human = input("rock, paper or scissors ? ")

    if human != "rock" and human != "paper" and human != "scissors":
        print("You chose something other than the requested commands!! \n You Lost !!")
        go_again = input("Wanna fo again ? (y/n) : ").lower()
        if go_again == "y":
            rock_paper_scissor()
        else:
            print("Goodbye")
            return None

    print(f"You: \n {eval(human)}")
    pc = random.choice([rock, paper, scissors])
    print(f"Pc: \n{pc}")


    if (pc == eval(human)):
        print(" Draw !! Go again ")
    elif (pc == rock and eval(human) == scissors) or (pc == scissors and eval(human) == paper) or (pc == paper and eval(human) == rock):
        print(" You Lost !!")
    else:
        print("You Won !!")
    
    go_again = input("Wanna fo again ? (y/n) : ").lower()
    if go_again == "y":
        rock_paper_scissor()
    else:
        print("Goodbye")
        return None

rock_paper_scissor()