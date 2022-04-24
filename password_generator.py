#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password_length = nr_letters + nr_symbols + nr_numbers

len_letters = len(letters)
len_numbers = len(numbers)
len_symbols = len(symbols)

def rand_letter():
    letter_index = random.randint(0,len_letters-1)
    return letters[letter_index]

def rand_number():
    number_index = random.randint(0,len_numbers-1)
    return numbers[number_index]

def rand_symbols():
    symbol_index = random.randint(0,len_symbols-1)
    return symbols[symbol_index]

password=""
for letter in range(0,nr_letters):
    password = password + rand_letter()

for number in range(0,nr_numbers):
    password = password + rand_number()

for symbol in range(0,nr_symbols):
    password = password + rand_symbols()

# shuffle password
final_password = ''.join(random.sample(password,len(password)))

print("Random Password Generated:")
print(final_password)
