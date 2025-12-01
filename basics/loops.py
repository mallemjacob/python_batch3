# loops
# while
# while i am at work, do your homework



# i_am_at_work = True

# if i_am_at_work:
#     print('Do you home work')

# while i_am_at_work:
#     print('Do you home work')
#     i_am_at_work = False
    

# count = 1
# count = count + 1 #2
# count = count + 1 #3

# count = 1 #2
# while count <= 10:
#     print(count) #1, 2.... 10
#     count = count + 1 # 2 + 1

# break
# while count <= 10:
#     if count == 5:
#         break
#     else:
#         print(count) #1
#         count = count + 1

# print('end')

#continue
# while count <= 10:
#     if count == 5:
#         count = count + 1 #6
#         continue
#     else:
#         print(count)
#         count = count + 1

# password_attempts = 0
# while True:
#     print('Enter your name:')
#     name = input() #exit
#     if name == 'joe':
#         while True:
#             if password_attempts < 5:
#                 print('Enter your password')
#                 password = input() #ll
#                 if password == 'fish':
#                     print('Welcome to your account')
#                     break
#                 else:
#                     password_attempts = password_attempts + 1
#                     continue
#             else:
#                 print('Too many attempts. Try again in 24 hours.')
#                 break
#     elif name == 'exit':
#         break
#     else:
#         print('Not joe')
#     break

# count = 1 #2
# while count <= 10:
#     print(count)
#     count = count + 1


# for loop = specific number of times
# for how many guests

# for i in range(10)

for num in range(10): #1,1,2...10
    if num == 7:
          continue
    else:
         print(num)      

print('the end of for loop')

# Expression = evaluates to a single value
# 2 + 2 #4
# 2000 + 5 + 15 #2020

# statement = a line in a program.



''' do these steps multiple times, until correct asnwer is given
ask user for name
ony after giving correct name, we have to ask password
if not ask his name again,
if he gives coreect name, then ask for password
if password is correct, welcome him
if password is incorrect, ask for password again '''