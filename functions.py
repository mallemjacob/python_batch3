# Functions

# def greet(name):
#     print('Welcome ' + name)  

# greet('julia')

# user defined functions
# function definition
# def add(num1, num2, num3): #parameters
#     #function body
#     print('hi')
#     return num1 + num2 + num3

# n1 = int(input('Enter number1: ')) #'2' -- 2
# n2 = int(input('Enter number2: '))
# n3 = int(input('Enter number3: '))

# #function calling
# print(add(n1, n2, n3)) # arguments


#Built-in functions
#print()
#len()
#input()
#int()
#float()
#str()

# def greet(p1='a1', p2='a2', p3='a3'):
#     print(p1, p2, p3)

# greet('x',p3='y',p2='z')

# print('hello', end='')
# print('welcome')
# print('hi')

# print('a','b','c', sep='+')



import time
while True:
    for i in range(5, 10):
        print(' ' * i, end='')
        print('*' * 8)
        time.sleep(0.5)
    for i in range(10, 5, -1):
        print(' ' * i, end='')
        print('*' * 8)
        time.sleep(0.5)

# count = 0
# indent = True
# while True:
#     print(' ' * count, end='')
#     print('*' * count)
#     time.sleep(0.1)

#     if indent:
#         count = count + 1
#         if count == 10:
#             indent = False
#     else:
#         count = count - 1
#         if count == 0:
#             indent = True