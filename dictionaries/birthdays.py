birthdays = {
    'Alice': 'Apr 1',
    'Bob': 'Dec 12',
    'Carol': 'Mar 4',
    'Bottle': 'Jan 1'
    }

while True:
    print('Enter a name: (blank to quit)')
    name = input() # 'Pen'
    if name == '': # '' == ''
        break

    elif name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
            
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        bday = input() # Jan 1
        birthdays[name] = bday 
        # birthdays['Bottle'] = 'Jan 1'
        print('Birthday database updated.')


print(1 + 1)