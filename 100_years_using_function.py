def age():
    name = input("Enter your name")
    age = int(input("Enter your age"))
    years_left = 100 - age
    year = 2021 + years_left
    print(name, 'You become 100 years in', years_left, 'years i.e, in the year', year)

age()
