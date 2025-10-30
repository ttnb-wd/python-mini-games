import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0','1', '2','3','4','5', '6', '7','8','9']
symbols = ['!', '#','$', '%', '&', '(',')', '*', '+']

letters_count = int(input("How many letters would you like in your password?\n"))
numbers_count = int(input("How many numbers would you like in your password?\n"))
symbols_count = int(input("How many symbols would you like in your password?\n"))

letters_list = []
numbers_list = []
symbols_list = []

for i in range(letters_count):
    letter = letters[random.randint (0, len(letters) - 1)]
    letters_list.append(letter)
    
for i in range(numbers_count):
    number  = numbers[random.randint (0, len(numbers) - 1)]
    numbers_list.append(number)
    
for i in range(symbols_count):
    symbol = symbols[random.randint (0, len(symbols) - 1)]
    symbols_list.append(symbol)
    
password_list = letters_list + numbers_list + symbols_list
random.shuffle(password_list)
password = "" .join(password_list)
print(f"Your password is: {password}")
