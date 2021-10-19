############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

# Level = Beginner

import random
from art import logo

# The last three 10's represent the Queen, King and Jack cards and 11 is the Ace.
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

hit = "y"
go_again = "y"

def deal(player, k):
    """ deals k cards to player """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]    
    player += random.choices(cards, k = k)


def check_for_ace(player):
    """Checks if there is an ace in the player's hand and replace ir with 1 if sum(player) > 21"""
    if 11 in player and sum(player) > 21:
        ix = player.index(11)
        player[ix] = 1


def above21(player):
    """ Checks if sum(player) > 21"""
    if sum(player) > 21:
        return True
    return False


def score(player, dealer):
    """ checks and returns the result of the game """
    if above21(player):
        print(f"Dealer's cards were : {dealer} => Total score : {sum(dealer)}")
        print(f"Your cards were : {player} => Total score : {sum(player)}")
        print("Bust !! You Lost ")

    elif above21(dealer):
        print(f"Dealer's cards were : {dealer} => Total score : {sum(dealer)}")
        print(f"Your cards were : {player} => Total score : {sum(player)}")
        print("Bust !! You Won ")
    
    elif 11 in player and 10 in player and len(player) == 2:
        print(f"Dealer's cards were : {dealer} => Total score : {sum(dealer)}")
        print(f"Your cards were : {player} => Total score : {sum(player)}")
        print("Blackjack !! You Won")

    elif 11 in dealer and 10 in dealer and len(dealer) == 2:
        print(f"Dealer's cards were : {dealer} => Total score : {sum(dealer)}")
        print(f"Your cards were : {player} => Total score : {sum(player)}")
        print("Dealer has a Blackjack !! You Lost")

    elif sum(player) > sum(dealer):
        print(f"Dealer's cards were : {dealer} => Total score : {sum(dealer)}")
        print(f"Your cards were : {player} => Total score : {sum(player)}")
        print(" You Won !!")

    elif sum(player) == sum(dealer):
        print(f"Dealer's cards were : {dealer} => Total score : {sum(dealer)}")
        print(f"Your cards were : {player} => Total score : {sum(player)}")
        print("Draw !!")

    else:
        print(f"Dealer's cards were : {dealer} => Total score : {sum(dealer)}")
        print(f"Your cards were : {player} => Total score : {sum(player)}")
        print("You Lost !!")


def game_continues(player, dealer):
    """ checks  if the game should continue based on the rules"""

    if above21(player):
        return False

    elif above21(dealer):
        return False
    
    elif 11 in player and 10 in player and len(player) == 2:
        return False
    
    else:
        return True
        

def Blackjack():
    """ the blackjack game """
    print(logo)
    player = []
    dealer = []

    deal(player, 2)
    deal(dealer, 2)

    check_for_ace(player)
    check_for_ace(dealer)

    while game_continues(player, dealer):

        print(f"Dealers cards are : [{dealer[0]}, *] ")
        print(f"Your cards are {player}, current scor = {sum(player)}")

        hit = input("Do you want another card? (y/n) : ")
        while hit == "y":
            deal(player, 1)
            check_for_ace(player)
            print(f"Your cards are {player}, current scor = {sum(player)}")
            if not game_continues(player, dealer):
                break
            hit = input("Do you want another card? (y/n) : ")

        else:
            while sum(dealer) < 17:
                deal(dealer, 1)
                check_for_ace(dealer)

            print(f"Dealers cards are : [{dealer[0]}, *] ")
            print(f"Your cards are {player}, current scor = {sum(player)}")

            if hit != "y" and sum(dealer) >= 17:
                break

    score(player, dealer)

    go_again = input("Wanna go again? (y/n): ")
    if go_again == "y":
        Blackjack()
    else:
        print("Good Bye!")
        return None


play = input(" Do you want to play a Blackjack game?(y/n) : ")
if play == "y":
    Blackjack()