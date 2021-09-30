'''4. Take two lists, say for example these two:
 a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
 b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common
between the lists (without duplicates). Make sure your program works on two lists of different
sizes.'''

#Method1
a = [1, 1, 2, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
a1=set(a)
b1 = set(b)
print(type(a1))
print(a1.intersection(b1))

#Method2
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
for a1 in a:
    for b1 in b:
        if a1 == b1:
            if a1 not in c:
                c.append(a1)
print(c)