# This program helps you to generalize a strong password based on the number of characters, numbers and symbols you want to be in your password.
# Level = Beginner

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# The choises here are simply taken from user!! but user can input some wrong combination
# for example if user inputed 72 for number of characters he/she wants for his/her password
# when there are  71 characters in total
# this problems can be easily fixed by adding some conditions to code to raise errors when such things happen.

print("Welcome to passwoed generator ")
n_letters = int(input(" How many characters you want your password to be? "))
n_symbols = int(input(" How many symbols you want your password to have? "))
n_numbers = int(input(" How many numbers you want your password to have? "))

pass_letters = random.choices(letters, k=n_letters - (n_symbols + n_numbers))
pass_symbols = random.choices(symbols, k=n_symbols)
pass_numbers = random.choices(numbers, k=n_numbers)

password_list = pass_letters + pass_symbols + pass_numbers
random.shuffle(password_list)
password = ""
for i in range(0, n_letters-1):
    password += password_list[i]

print(f"Your password is : {password}")