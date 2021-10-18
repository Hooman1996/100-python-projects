# This program is used to encode and decode messages using a specific shift in alphabets.

# Level = Beginner

# The alphabet list is written 2 times back to back so there will be no problem if the letters in the message were at the end of the list when encoding the text.
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

from art import logo
print(logo)

def caesar(direction, text, shift):
    output = ""
    shift = shift % 26
    if direction == "decode":
        shift *= -1
    for letter in text:
        if letter not in alphabet:
            output += letter
        else: 
            ix1 = alphabet.index(letter) # the letter's index in alphabet
            ix2 = ix1 + shift # the letters index in alphabet after shifting
            output += alphabet[ix2]

    print(f"The {direction}d text is: {output}")

go_again = "yes"
while go_again == "yes":
    direction = input(" Inpute 'encode' to encrypt, type 'decode' to decrypt : \n")
    text = input("Type your message : \n")
    shift = int(input("Type the shift number :\n "))
    caesar(direction, text, shift)
    go_again = input("Wanna go again? type 'yes' if you want to go again, otherwise type 'no'.\n")
    if go_again == "no":
        print("Good Bye")