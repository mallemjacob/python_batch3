spam = "Hello world's"
print(spam)

# escape character
spam = 'Hello world\'s'
print(spam)

# \n = newline
# \t = tab
# \\ = backslash

spam = 'hi\nthere'
spam = 'hi\tthere'
spam = 'hi\\there'
print(spam)

path = 'C:\\Users\\Al\\programs'
print(path)

# raw strings
print(r"C:\\Users\\Al\\programs")

# triple quotes
spam = '''hi 



                there'''

spam = 'hi\n\n\n\n\t\t\tthere'

print('Line 30:', spam)

def greet(a):
    """
    This function return a greeting to the user.

    It take a one argument.
    """
    return 'hi ' + a

print(greet('pink'))

# List
spam = ['cat','bat','mat']
print(spam[0])
print('cat' in spam)

#string indexes
spam = 'hi there'
print(spam[0])
print(spam[0:2])
print(spam[-5:])

print('hi t' in spam)
print('ere' in spam)

print('cat' not in spam)
print('cat' in spam)

# f-strings
name = 'chanel'
age = 20
print('hi there ' + name + ' Your age is ' + str(age))
print(f"hi there {name} Your age will be {age + 1} next year.")

''' Methods
    ---------- '''

# Upper
spam = 'hi there'
print(id(spam))
print(id(spam.upper()))

print(spam.upper())

spam = 'HI THERE'
print(spam.lower())

print('Enter a username: ')
username  = input() # 'Black
if username.lower() == 'black':
    print('Welcome')

print(spam.islower())
print(spam.isupper())

# isalpha
spam = 'hithere'
print(spam.isalpha())

if not spam.isalpha():
    print('Password must only contain letters and not numbers')
else:
    print('Password set successfully')

# isalnum

spam = 'black 123'
print(spam.isalnum())

# isdecimal
spam = '12345'
print(spam.isdecimal())

# print('Enter a number: ')
# number  = input() # 'Black
# if number.isdecimal():
#     print('Welcome')

# isspace = space, tab, newline
spam = '    '
print(spam.isspace())

# istitle
spam = 'hi there' #False
spam = 'Hi There' #True
spam = 'HI There' # False
print(spam.istitle())

# Methods chanining

spam = 'hi there'
print(spam.upper().isupper())