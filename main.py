import random

number_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
symbol_list = ["!", "@", "#", "$", "&"]
wordlist = open("wordlist.txt", "r").read().split('\n')


def generate_password(num_amount, add_symbol):
    word1 = random.choice(wordlist).capitalize()
    word2 = random.choice(wordlist).capitalize()
    number = generate_numbers(num_amount)
    if add_symbol == "Y":
        symbol = random.choice(symbol_list)
    else:
        symbol = ""

    password = word1 + word2 + number + symbol
    return password

def generate_numbers(num_amount):
    number = ""
    while num_amount != 0:
        num = str(random.choice(number_list))
        number += num
        num_amount -= 1
    return number
        
print("How many passwords would you like to generate?")
amount = int(input())
print("How many numbers would you like in your passwords?")
num_amount = int(input())
print("Would you like a symbol? Y/N")
add_symbol = input().upper()
print("Generating passwords...")


while amount != 0:
    password = generate_password(num_amount, add_symbol)

    print(password)
    amount -= 1


