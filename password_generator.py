import random
import string

print("Welcome to password generator")
num_of_letters=int(input("Enter the number of letters you want in your password:"))
num_of_symbols=int(input("Enter the number of symbols you want in your password:"))
num_of_integers=int(input("Enter the number of numbers you want in your password:"))
char=''
num_list = []
for i in range(num_of_integers):
    char=char+str(random.randrange(0,10))
list_of_symbols = ['@','!','#','$','%','^','&','*','(',')']
for i in range(num_of_symbols):    #
    char+= random.choice(list_of_symbols)
for i in range(num_of_letters):
    char+= random.choice(string.ascii_letters.lower())

list_of_password=list(char)
print(list_of_password)

random.shuffle(list_of_password)
# print(list_of_password)
str=''
for item in list_of_password:
    str+=item
print(str)


