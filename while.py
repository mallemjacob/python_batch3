# While loop
# i = 0
# while i < 2:
#     print('hi')
#     i = i + 1

# for loop
# for i in range(5): # 0,1,2,3,4
#     print(i)

# for i in range(5, 10):
#     print(i)


# break 
# while True:
#     print('Enter name:')
#     name = input() #bill
#     if name == 'julia':
#         print('Hi julia')
#         break
#     else:
#         print('not julia')

# for i in range(10): # 0, 1,2, 3, 4, 5
#     if i == 5:
#         break
#     else:
#         print(i)

# print('the end')


#continue
# i = 0
# while i < 10:
#     if i == 5: # 0 == 5
#         i = i + 1
#         continue
#     else:
#         print(i)
#         i = i + 1 # 0 + 1

# print number from 5
# for i in range(10):
#     if i < 5: 
#         continue
#     else:
#         print(i)

# skip mutiples of 3
# for i in range(10):
#     if i % 3 == 0: 
#         continue
#     else:
#         print(i)

# skip number 37
# for i in range(1, 101):
#     if i == 37: 
#         continue
#     else:
#         print(i)

#print numbers in reverse
# for i in range(10, 0, -1):
#     print(i)

#print every 3rd numbers
# for i in range(0, 10, 3): # 0 1 2 3 4 5 6 | 0 2 4 6 8
#     if i == 6:
#         break
#     else:
#         print(i)

# stop the infinite loop with ctrl + c

# using for-loop in a while loop
# while True:
#     for i in range(10): # 0 1 2 3 4 5 6 7 8 9
#         if i == 4:
#             break
#         else:
#             print(i)
#     break            


# using while and for loops in a if statement.

# print('Enter a number:')
# user_num = int(input()) # '2' int()

# if user_num == 2:
#     print('This is a for loop')
#     for i in range(10):
#         print(i)
# else:
#     print('This is a while loop')
#     i = 0
#     while i < 10:
#         print(i)
#         i = i + 1     

password_counter = 1
while True:
    print('Enter name:')
    name = input() #bill
    if name == 'julia':
        print('Hi julia')
        while True:
            print('Enter your password')
            password = input() # fish
            if password == 'fish':
                print('Welcome to your account!')
                break
            else:
                if password_counter != 5:
                    print('Please enter correct password!')
                    password_counter += 1
                    continue
                else:
                    print('You have used all of your chances.')
                    break
                    
    else:
        print('Enter correct username')
        continue
    break

# break 
# counter = 3
# for i in range(counter):
#     print('Enter name:')
#     name = input() #bill
#     if name == 'julia':
#         print('Hi julia')
#         break   
#     else:
#         if i == counter - 1:
#             print('You have completed your chances!')
#         else:
#             print('not julia')
#             print('You have only ' + str(counter - (i + 1)) + ' chances left.')