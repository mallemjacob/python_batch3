# while True:
#     print('Enter your name:')
#     name = input() 
#     if name == 'joe': #joe == joe,  exit
#         print('hi joe')
#         while True:
#             print('Enter your password:')
#             password = input()
#             if password == 'fish':
#                 print('welcome to your account')
#                 break
#             else:
#                 print('wrong password! try again!')
#     elif name == 'exit':
#         break                                
#     else:
#         print('not joe. try again')
        

# print('the end')

# print('Start of for loop')

# for num in range(10): #0,1,2...9
#     if num == 5:
#         continue
#     else:
#         print(num)      

# print('the end of for loop')


for i in range(10): #0,1
    print('Enter your name:')
    name = input() 
    if name == 'joe': #joe == joe,  exit
        print('hi joe')


        # ********************************
        #inner loop
        for i in range(5): # 0,1,2,3,4
            print('Enter your password:')
            password = input()
            if password == 'fish':
                print('welcome to your account')
                break
            else:
                print('wrong password! try again!')
        # ********************************


    elif name == 'exit':
        break                                
    else:
        print('not joe. try again')
        

print('the end')