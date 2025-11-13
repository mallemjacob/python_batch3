# list = ['cat','bat','mat']
# #         0     1     2

# list[0] = 1

# # print(list)

# dictionary = { 'name' : 'mouse', 'age' : 5, 12345 : 'password' }

# print(dictionary['name'])

# dictionary['age'] = 7

# print(dictionary.keys())
# print(dictionary.values())
# print(dictionary.items())

# for i,j in dictionary.items():
#     if j == 'mouse':
#         print(i)

# for k in dictionary.keys():
#     print(k)

# for v in dictionary.values():
#     print(v)

# spam = {
#     'colors': ['black','grey','blue'],
#     'titles':[
#         {
#         "name": "public-apis"
#         },{
#         "name": "MIT License"
#         },{
#         "name": "free-programming-books"
#         }
#     ],
#     'ids': {
#         'year' : 2025,
#         'list_of_ids' : [1,2,3,4,5]
#     }
# }
# print(spam['titles'][-1]['name'])

# for i in spam['titles']:
#     print(i["name"])

# print(spam['colors'][0])
# print(spam['ids']['list_of_ids'][-1])

# for i in spam['ids']['list_of_ids']:
#     print(i)

# json --> python dict



# create an empty books dictionary (title, pages)
# take user input
# check if the key exists in the dictionary
# then print that value
# if it dont exists, ask the value for that key
# Add that key and value to the dictionary.

books = {}

print('Books database: ')

while True:
    title = input('Enter a book title: ') #stranger
    if title == '':
        break
    else:
        if title in books:
            print(books[title])
        else:            
            print('The book doesnt exists')
            pages = input('Enter number of pages: ') #92
            books[title] = pages
            #books['stranger'] = 92

print('The book database contains: ')
for book, pages in books.items():
    print('Book: ' + book + ' , ' + 'Pages: ' + pages)