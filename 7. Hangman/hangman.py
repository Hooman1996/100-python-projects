# The code implementation of the hangman game.
# in this game the first player chooses a word and the second player will be given a limited number of chances to guess the letters in the word.
# every time the second player chooses a letter, the game will check if the letter exists in the word and show it if ist there.
# if not our poor man will get one step closer to death.
# Saw movie vibes right? :)

# in this code, because there will be only one person to play(the user) the first world will be chosen from a list of random words
# you can change the world or even ask the user to input it for you.

import random
from hangman_words import word_list
from hangman_art import logo, stages

print(logo)

chosen_word = random.choice(word_list).lower()
number_of_characters = len(chosen_word)

guessed_letters = ["_" for letter in chosen_word]

lives = len(stages)
while lives > 0:
    print(guessed_letters)
    guessed_letter = input("Guess a letter : ").lower()
    if guessed_letter in guessed_letters:
        print(" You already picked this letter!! choose another ")
        continue 
    if guessed_letter in chosen_word:
        print(f"The letter {guessed_letter} is in the word ")
        for i, letter in enumerate(chosen_word):
            if letter == guessed_letter:
                guessed_letters[i] = guessed_letter
        if not "_" in guessed_letters:
            print("You Won!")
            break
    else:
        lives -= 1
        print(f"The letter you chosed was not in the word. \nYou have {lives} chances left")
        print(stages[lives])
else: 
    print(f"Game Over!! The word was {chosen_word}")

