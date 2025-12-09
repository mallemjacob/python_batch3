spam_list = ['cat','bat']
             # 0     1

spam_list[0]  # 'cat                          

spam_dic = {
    1 : 'fat',
    0.1 : 'gray',
    'disposition': 'loud'
    }     

print(spam_dic[1])  
print(spam_dic[0.1])
print(spam_dic['disposition'])      


animals1 = {
    'name': 'mouse',
    'age': 5,
    'sizes': [5,7,9]
}

animals2 = {
    'name': 'cat',
    'age': 7,
    'sizes': [12,18,24]
}

animals_list_of_profiles = [animals1, animals2]

print(animals_list_of_profiles[0]['sizes'][2]) #9


