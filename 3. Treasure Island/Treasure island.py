# This is a game in which choosing between different actions will lead to different scenarios
# Noting like Red dead redemption 2 but still ;)

# Level = Beginner

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
''')

# Greeting
print("Welcome to Treasure island.\n Your mission is to find the treasure")

# The choises will seperate the route the player takes using the Conditional statements

choice1 = input("You're at a cross road. Where do you want to go? left or right : ")
if choice1.lower() == "left":
    choice2 = input("You've come to a lake. There is an island in the middle of the lake. type 'wait' to wait for a boat or 'swim' to swim there : ")

    if choice2.lower() == "wait":
        choice3 = input("You arrived at the island safely. There is a house in the island with three doors. red, yellow and blue!! which door? ")

        if choice3.lower() == "red":
                print("Thats a room full of fire!! \n Game Over")
        elif choice3.lower() == "blue":
            print("You walked into a trap!! \nGame Over")
        elif choice3.lower() == "yellow":
            print("You found the treasure chest!! You Win !! ")

    else:
        print("You got attacked by a angry crocodile!! \nGame Over")   
else:
    print(" You fell into a hole !! \n Game Over ")

