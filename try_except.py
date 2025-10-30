# while True:
#     try:
#         user_input = int(input('Enter a number: '))
#         if user_input == 0:
#             break
#         print(f"You entered: {user_input}")
#     except ValueError:
#         print('Must be interger. Try again!')    

# while True:
#     try:
#         user_input = int(input('Enter a number: '))
#         print(f"You entered: {user_input}")
#         break
#     except ValueError:
#         print('Must be Interger!')
#     except TypeError:
#         print('Both values must be integres!')
#     except KeyboardInterrupt:
#         print('The end')
#         break

try:
    val = input() #2
    print(2 + val)
except TypeError:
    print('Must be integer!')
except ValueError:
    print('')  

print('end')