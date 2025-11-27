spam = 'hi there'
print(spam.title())

print(spam.capitalize())

print(spam.startswith('hi'))
print(spam.endswith('re'))

print('|'.join(['red','green','blue']))
print(' '.join(['red','green','blue']))
print(' and '.join(['red','green','blue']))

print('hi there'.split(' '))
print('hi there'.split('e'))
print('hi,bye,welcome'.split(','))

print('hi,bye,welcome'.partition(','))

spam = 'cat'
print(len(spam)) #3
new_rspam = spam.rjust(15)
print(new_rspam)
print(len(new_rspam))

new_lspam = spam.ljust(15)
print(new_rspam)
print(len(new_rspam))

print('hello'.replace('ll','rr'))
