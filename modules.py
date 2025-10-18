
#Modules
#Math
#Random

# import random

# print(random.randint(1, 10))

# import math

# print(float(math.sqrt(2)))

# import random

# while True:
#     print('Outer loop')
#     ran_num = random.randint(1,10) #5
#     while True:
#         print('Inner loop')
#         iinp = int(input('Enter inner input between 1 and 10: ')) # 5
#         if iinp == ran_num: # 6 == 5
#             sys.exit()


# while True:
#     print('Type exit to exit.')
#     response = input()
#     if response == 'exit':
#         sys.exit()
#     print('You typed ' + response + '.')


# Guess the number

import random
random_number = random.randint(1, 20) # 10
counter = 0

while True:
    print('I am thinking of a number between 1 and 20.')
    print('Take a guess.')
    user_input = int(input()) # '5' --> 5
    counter = counter + 1
    if user_input < random_number:
        print('Your guess is too low.')
    elif user_input > random_number:
        print('Your guess is too high.')
    elif user_input == random_number:
        print('Good job! You guessed my number in ' + str(counter) + ' chances.')
        break
