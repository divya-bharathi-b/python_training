'''FOR LOOP'''
animals = ['cat', 'dog', 'fish', 'tiger']
for i in animals:
    print(i, len(i))

#speicfy single digit range shows
for animals in range(4):
    print('d')
    print(animals)

for animals in range(1, 4):
    print('d')
    print(animals)

for animals in range(0, 4, 2):
    print('d')
    print(animals)

''' WHILE LOOP'''
i = 3
while i < 15:
    print("Hey")
    i = i + 3

a = 2
while a < 20:
    print(a * 2)
    a = a + 1