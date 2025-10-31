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
print('hi ' + 'there') # 'hi there'
# List concatenation
print([1,2] + [3,4]) # [1,2,3,4]

spam = []

user_input = input() #cat
spam = spam + [user_input]
# ['dog'] + ['cat'] # ['dog', 'cat']

spam = spam + ['keyboard']

spam = ['monitor'] + spam

print(spam)


# create a new empty list
# create a while loop
# take user input and store it in a variable
# if user types "exit", break the loop
# else concatenate the user input to the empty list.
# finally print the list items with for loop

