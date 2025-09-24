# Find Prime Number

# Library
from os import system as sys
from termcolor import colored
from pyfiglet import figlet_format

# Clear Terminal
sys('clear')

# Intro
print(colored(figlet_format('Welcome'), color='cyan'))
print(colored('========================================', color='red'))
print(colored('This program for detecting prime number', color='cyan'))
print(colored('=======================================', color='blue'))
print('                                                             ')

# While True
while True:

    # Value Input
    number = int(input(colored('Enter Number ===> ', color='light_red')))
    prime = True

    # Loop
    for i in range(2, number):
        if number % i == 0:
            prime = False

    # IF For Prime Number
    if prime:
        print(colored(figlet_format(
            f'{number} Is Prime'), color='green'))

    # Else For Not Prime Number
    else:
        print(colored(figlet_format(
            f'{number} Is Not Prime'), color='red'))

    # Value For Try Again
    con = input('Do you want try again [y/n] ===> ')

    # IF For Continue
    if con == 'y' or con == 'Y':
        continue
    # Elif For Break Program
    elif con == 'n' or con == 'N':
        break
    # Else For Break Program
    else:
        break


# moeinit.com
# Create By Moein Heshmati
# Finish
