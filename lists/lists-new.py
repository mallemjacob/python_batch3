# nums = [1,2,3,4,5]

# inches = [0.1,0.2,0.3]

# colors = ['red','white','blue']

# langs = ['german','french','russian']

# mixed = [1,2,True, 'true', 'mouse', ['big', 'small']]

# print(nums)
# print(inches)
# print(colors)
# print(langs)
# print(mixed)

#CRUD = create, read, update, delete

# creating a list
# food_items = ['grapes','apples']

# # reading a list
# print(food_items)

# # reading a list item
# print(food_items[0])

# # updating a list item
# food_items[0] = 'pears'
# print(food_items[0])
# print(food_items)

# # deleting a list item
# del food_items[0]
# print(food_items)
# print(food_items[0])

# looping through a list
langs = ['german','french','russian','spanish']


# for i in langs:
#     print(i)

# for i in range(len(langs)): #range(3) = 0,1,2
#     print(f"{i + 1}: {langs[i]}")  #langs[0], langs[1], langs[2]

for index, item in enumerate(langs):
    print(f"{index + 1}: {item}")

# 0 + 1 = 1
# 1 + 1 = 2
# 2 + 1 = 3

