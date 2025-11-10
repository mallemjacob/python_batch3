# Sequence data types
# lists = mutable
# strings = immutable
# tuples = immutable

spam = []
tiples = (1,2,3,4)
# tiples[0] = 'hi'

# name = 137386008970416 ---> 'mouse'
# cheese = 137386008970416 ---> 'mouse'
# print(id(name))
# print(id(cheese))

# name.append('s')
# name = name + 's'
# print(id(name))

# print(name)

# spam.append('h')

# print(tiples[0])
# print(spam[0])


# a = [1,2,3]
# b = a
# b[0] = 10

# print(a)
# print(b)

import copy
def greet(p):
    print(id(p))
    p.append('hi')

spam = [1,2,3,4,5]
newspam = copy.copy(spam)
greet(newspam)

print(id(spam))

print(spam)
print(newspam)