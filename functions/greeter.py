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




def hello(i): #function definition, i = parameter
    j = i + 1 # function body
    return j # returns to the calling function
    

print(hello(0)) # function calling, 0 = argument
print(hello(9))

    