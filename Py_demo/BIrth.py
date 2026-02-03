try:
    birth_year = input('Brith year: ')
    print(type(birth_year))
    age = 2026-int(birth_year)
    print(type(age))
    print(f'Your age is: {age}')
except ValueError:
    print("Please enter a valid number for birth year.")