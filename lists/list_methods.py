# List methods
#-------------

# spam = ['hello', 'hi', 'howdy', 'heyas'] #4

#index
# print(spam.index('howdy')) #2

# print('cat' in spam)

# if 'cat' in spam:
#   spam.index('cat')
# else:
#   print('cat not in index')  

# print(spam[0])
# print(spam.index('hello')) #0

# print(spam[spam.index('hello')]) # 'hello'

# spam.index('cat')

#append
# spam = ['cat', 'dog', 'bat']
# print(spam)
# spam.append('moose')
# print(spam)

#insert
# spam.insert(0, 'mmoose')
# print(spam)


#list concantnation +
# spam1 = [1,2]
# spam2 = [3,4]
# spam3 = spam1 + spam2 #[1,2,'spam2']
# print(spam3)

#remove
# spam = ['cat', 'bat', 'rat', 'elephant']
# spam.remove('cat')
# print(spam)

# spam = ['cat', 'bat', 'rat', 'cat', 'hat', 'cat']
# spam.remove('cat')
# print(spam)

# remove multiple cats
# for i in spam:
#     if i == 'cat':
#         spam.remove('cat')
# print(spam)

#sort
# spam = [2, 5, 3.14, 1, -7]
# spam.sort()
# print(spam)

# spam = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
# spam.sort()
# print(spam)
# spam.sort(reverse=True)
# print(spam)
# print(spam[::-1])

# sort uses ASCIIbetical order.
# spam = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']
# spam.sort()
# print(spam)

#sort by alphabetical order
# spam = ['a', 'z', 'A', 'Z']
# spam.sort(key=str.lower)
# print(spam)

# reverse
# spam = ['cat', 'dog', 'moose']
# spam.reverse()
# print(spam)

#append
spam = ['cat', 'dog', 'moose']
# spam.append('elephant')
# print(spam)

#clear
# spam.clear()
# print(spam)

# copy
# spam = ['cat', 'dog', 'moose']
# bacon = spam.copy()
# bacon[0] = 'pig'

# print(spam)
# print(bacon)

#count
# spam = ['cat', 'dog', 'moose','dog', 'dog']
# print(spam.count('moose'))

#extend
spam = ['cat', 'dog', 'moose']
spam.extend('123')
spam.extend(['a','b'])
print(spam)
spam.remove('a')
print(spam)
removed_value = spam.pop(0)
print(spam)
print(removed_value)