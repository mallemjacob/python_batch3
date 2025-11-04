# color1 = 'red'
# print("Line2: " + color1)

# color1 = 'blue'
# print("Line2: " + color1)

# spam = 'hi'
# print(len(spam))

# List value is the list with all items.
# List item is the items in the list.

# colors = ['red', 'blue', 'black']
# #           #0      #1       #2
# print("Line8: " + colors[2])


# random_items = [True, 1, 'hello', None]
# print(random_items[0])


# CRUD Operations -->
#create a new list
# numbers = [1, 2, 3, 4, 5, 6]
# spam = []

# #read a value from a list
# print(numbers[5]) # 6

# #update a value from list
# numbers[5] = 7
# print(numbers)
# numbers[5] = 8
# print(numbers)

# #delete a value from a list
# del numbers[0]
# print(numbers)


# check length of the list
          #-6  #-5   #-4   #-3    #-2    #-1  
# spam = ['cat','bat','mat','dog','mouse','pen']
         #0     #1    #2    #3    #4      #5
# print(spam)         
# print(len(spam))
# last_item = spam[len(spam) - 1]
# print(last_item)
# print(spam[-1])
# print(spam[-2])

# for i in spam:
#     print(i)

# for i in range(len(spam)):
#     # print(spam[i])
#     print("Index " + str(i) + " Value: " + spam[i])

# String concatnation
# print('hi ' + 'there') # 'hi there'
# # List concatenation
# print([1,2] + [3,4]) # [1,2,3,4]

# spam = []

# user_input = input() #cat
# spam = spam + [user_input]
# # ['dog'] + ['cat'] # ['dog', 'cat']

# spam = spam + ['keyboard']

# spam = ['monitor'] + spam

# print(spam)


# create a new empty list
# create a while loop
# take user input and store it in a variable
# if user types "exit", break the loop
# else concatenate the user input to the empty list.
# finally print the list items with for loop


# users = []
# while True:
#     print('Enter a name:')
#     user = input()
#     if user == 'exit':
#         break
#     else:
#         users = users + [user]


# print(users)
# for user in users:
#     print(user)


# spam = ['cat','bat','mat','dog']

# #append
# spam.append('mouse')

# #insert
# spam.insert(0, 'bird')
# print(spam)

# #remove --> pass list item to remove
# spam.remove('mouse')
# print(spam)

# #pop --> removes item and returns it, pass item index to remove.
# removed_item = spam.pop()
# print(removed_item)

# spam.pop(0)
# print(spam)

# #reverse
# spam.reverse()
# print(spam)

# #sorting list items
# spam.sort()
# print(spam)

# #extend --> merge multiple lists
# colors = ['black','grey','purple']
# spam.extend(colors)
# print(spam)

#clear
# spam.clear()
# print(spam)

#index
# b_index = spam.index('black')
# print(b_index)

# #count
# nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 44, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 44, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]


# n = nums.count(44)
# print(n)

# #copy a list
# nums_new = nums.copy()
# print(nums_new)

#pi progam (My version)
# def make_pi():
#     expecting_value = 3
#     pi_list = []
#     while True:
#         if len(pi_list) == 3:
#             break
#         else:
#             print('Enter numbers: 1 3 or 4')
#             user_input = int(input()) #1
#             if user_input == 1 or user_input == 3 or user_input == 4:
#                 if user_input == expecting_value:
#                     pi_list = pi_list + [user_input]
#                     if expecting_value == 3:
#                         expecting_value = 1
#                     else:
#                         expecting_value = 4
#                 else:
#                     print('The expecting value is: ' + str(expecting_value))
#             else:
#                 print('Must be 1, 3 or 4')

#     print(pi_list)

# make_pi() 

# pi program (gemini)
def make_pi_simple():
    # The target sequence of digits: [3, 1, 4]
    target_pi = [3, 1, 4]
    # List to store the user's correct inputs
    user_pi = []

    # Loop until the user has correctly entered all 3 digits
    for expected_digit in target_pi:
        while True:
            print(f'Enter the next number to build Pi: 3, 1, or 4 (expecting {expected_digit})')

            try:
                # Get and convert the user's input to an integer
                user_input = int(input())
            except ValueError:
                # Handle cases where the input isn't a valid number
                print('Invalid input. Please enter a number.')
                continue # Go back to the start of the inner loop

            # 1. Check if the input is one of the allowed numbers (3, 1, or 4)
            if user_input not in [3, 1, 4]:
                print('Must be 1, 3 or 4.')
            # 2. Check if the input is the correct number for this step
            elif user_input == expected_digit:
                user_pi.append(user_input) # Add the correct digit to the list
                print(f'Correct! Current Pi: {user_pi}')
                break # Exit the inner 'while' loop to move to the next digit
            # 3. If it's an allowed number but not the correct one for the step
            else:
                print(f'Incorrect. The expecting value is: {expected_digit}')

    # After the loop finishes, the user_pi list will be [3, 1, 4]
    print(f'\nCongratulations! You built Pi: {user_pi}')

# Run the simplified function
make_pi_simple()