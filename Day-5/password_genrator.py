#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

if nr_letters < nr_numbers + nr_symbols:
    print(" You have exceded the limit for symbols and numbers!")

# easy level

password = ""

# for symbols
for item in range(0,nr_symbols):
    random_index_for_symbols = random.randint(0,len(symbols) - 1)
    password += symbols[random_index_for_symbols]

# for numbers
for item in range(0,nr_numbers):
    random_index_for_numbers = random.randint(0,len(numbers) - 1)
    password += numbers[random_index_for_numbers]

# for characters if password is short
characters_remaning = nr_letters - (nr_numbers + nr_symbols) 

if characters_remaning > 0:
    for item in range(0,characters_remaning):
        random_index_for_character = random.randint(0, len(letters))
        password += letters[random_index_for_character]
    

print(f"Your password \n {password}")


