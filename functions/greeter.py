# Code reusability
# Encapsulation
# Code modularity

# Bulit-in function
# print()
# input()

# user-defined function
# def greet(name, age):
#     print('Hello ' + name + '. You are ' + str(age) + ' years old.')

# greet('Mouse', 5)
# greet('Bat',7)

# def d():
#     print('d')

# def b():
#     print('b')

# def c():
#     print('c')
#     d()

# def a():
#     print('a')
#     b()
#     c()
#     return 'final a()'

# output = a()
# print(output)

# a() -> b() -> a() -> c() -> d() -> c() -> a()

# user-defined function
# def greet(name='Dracual', age=3000):
#     msg = 'Hello ' + name + '. You are ' + str(age) + ' years old.'
#     return msg

# print(greet('Mouse', 5))
# print(greet())


# nameofarg = 'keyboard'

# print(greet(nameofarg, len(nameofarg)))  # 'Bat', 3


# def checkHeight(height):
#     inch_to_cm = 2.54
#     convertToCms = height * inch_to_cm
#     output = round(convertToCms, 2)
#     return output

# checkHeight(5.11)


# def start(score=0, kills=0):
#     print('Game started')
#     print(f'You score is {score}')
#     print(f'You have killed {kills} enemies')
    
# start(score=10, kills=3)




# def hello(i): #function definition, i = parameter
#     j = i + 1 # function body
#     return j # returns to the calling function

# print(hello(0)) # function calling, 0 = argument
# print(hello(9))

# If you don't explicitly return a value from the function, it returns None.


# def adder(a1=1,a2=1):
#     print(a1)
#     print(a2)

# adder(a2=2,a1=3)

#*args
# def adder(*nums):
#     total = 0
#     for i in nums:
#         total = total + i
#     print(f"{nums}: {total}")

# adder(1,2,3) #6
# adder(1,2,3,4,5) #15
# adder(1,2,3,4,5,6,7,8,9,10) #55

# def adder(a,b,*nums):
#     print(a)
#     print(b)
#     print(nums)

# adder(1,2,3,4,5)

# **kwargs
# def get_user_details(**details):
#     for key, value in details.items():
#         print(f"{key}: {value}")
#     print('----------')   

# get_user_details(name='Bobby', age=21, city='New York')
# get_user_details(name='Mouse', age=5, city='tennesse', score=10)


# def get_user_details(a,b,*nums,**details):
#     print(a)
#     print(b)
#     print(nums)
#     print(details)

# get_user_details(1,2,3,4,5,name='Bobby', age=21, city='New York')

