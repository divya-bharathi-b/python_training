def birthday(inp):
    if inp == 'Albert Einstein':
        print(inp, 'birthday is ', data['Albert Einstein'])
    elif inp == 'Benjamin Franklin':
        print(inp, 'birthday is ', data['Benjamin Franklin'])
    elif inp == 'Ada Lovelace':
        print(inp, 'birthday is ', data['Ada Lovelace'])
    else:
        print("The input you gave is not in our dictionary please recheck")


data = {'Albert Einstein': '14/03/1979', 'Benjamin Franklin': ' 01/17/1706', 'Ada Lovelace': '10/12/1815'}
print('Welcome to the birthday dictionary. We know the birthdays of:\nAlbert Einstein\nBenjamin Franklin')
inp = input("Who's birthday do you want to look up?")
birthday(inp)

'''data = {'name': ['Albert Einstein', 'Benjamin Franklin', 'Ada Lovelace'], 'dob': ['14/03/1979',' 01/17/1706','10/12/1815']}
print(data)
print()
names_list=data.get('name', '')
birthday_list=data.get('dob', '')
print(names_list, birthday_list)
print()'''
