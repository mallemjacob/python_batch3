#Scope

# Global scope is created when the program starts.
# There is only one globle scope.
# You can access varibles defined in global scope from anywhere 
# in the program.

#Local scope
# It is created when function is called.
# You can only access varibles inside the function defined in that function.
# You cannot access varibles from the globle scope defined in any function.
# val = 1


# def hello():
    #Local
    # val2 = 3
    # print("Inside hello() function: " + str(val2))
    # print("Inside hello() function: " + str(val))



# def greet():
#     global val
#     val = 6
#     hello()
#     print(val)
# greet()

# print(val)

# print("Outside hello() function: " + str(val))
# print("Outside hello() function: " + str(val2))




def a(p):
    val = 2
    val = val + p
    return val

ov = a(4)
print(ov)

while True:
    name = 'mouse'
    break

for i in range(2):
    name = 'mouse1'

print(name)

# print(val)

print()
int()
len()
str()