#PasswordGenerator
import random

chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

number = input('Number of passwords? - ')
number = int(number)

lenght = input('Passwor lenght? - ')
lenght = int(lenght)

for p in range(number):
    password = ''
    for c in range(lenght):
        password += random.choice(chars)
    print(password)