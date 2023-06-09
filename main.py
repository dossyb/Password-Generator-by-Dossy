import random

number_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
symbol_list = ["!", "@", "#", "$", "&"]
wordlist = open("wordlist.txt", "r").read().split('\n')


def generate_password(word_amount, num_amount, add_symbol):

    password = ""

    words = generate_words(word_amount)
    password += words
    number = generate_numbers(num_amount)
    password += number
    if add_symbol == "Y":
        symbol = random.choice(symbol_list)
    else:
        symbol = ""

    password += symbol
    return password

def generate_words(amount):
    password = ""
    words = [""] * amount
    for word in words:
        while len(word) < 4 or len(word) > 9:
            word = random.choice(wordlist).capitalize()
        password += word
    return password

def generate_numbers(amount):
    number = ""
    while amount != 0:
        num = str(random.choice(number_list))
        number += num
        amount -= 1
    return number

def get_pwd_amount():
    print("How many passwords would you like to generate?")
    pwd_amount = input()
    is_int = pwd_amount.isnumeric()
    while is_int == False or int(pwd_amount) > 1000 or int(pwd_amount) <= 0:
        print("Please enter a valid amount:")
        pwd_amount = input()
        is_int = pwd_amount.isnumeric()
    pwd_amount = int(pwd_amount)
    return pwd_amount

print("Welcome to Dossy's Password Generator!")
print("\n")
print("Note: the maximum amount of passwords that can be generated at one time is 1000") 
pwd_amount = get_pwd_amount()
print ("How many words would you like in your password? (min 1, max 5)")
word_amount = int(input())
while word_amount > 5 or word_amount <= 0:
    print("Please enter a valid amount:")
    word_amount = int(input())
print("How many numbers would you like in your passwords? (max 10)")
num_amount = int(input())
while num_amount > 10 or num_amount < 0:
    print("Please enter a valid amount:")
    num_amount = int(input())
print("Would you like a symbol? Y/N")
add_symbol = input().upper()
while add_symbol != "Y" and add_symbol != "N":
    print("Please enter a valid option (Y or N):")
    add_symbol = input().upper()
print("Generating passwords...")


while pwd_amount != 0:
    password = generate_password(word_amount, num_amount, add_symbol)

    print(password)
    pwd_amount -= 1


