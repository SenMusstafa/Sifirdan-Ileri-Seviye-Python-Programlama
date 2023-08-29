def sayHello(name='user'):
    return 'Hello ' + name

msg = sayHello('Mustafa')
print(msg)

def total(num1, num2):
    return num1 + num2

result = total(20, 10)
print(result)

def calculateAge(birth_year):
    return 2023 - birth_year

ageMustafa = calculateAge(1965)
print(ageMustafa)

def yearsToRetirement(birth_year, name):
    '''
    DOCSTRING: Calculates the number of years remaining until retirement based on the birth year.
    INPUT: Birth year
    OUTPUT: Calculated year information
    '''
    age = calculateAge(birth_year)
    retirement_years_left = 65 - age
    if retirement_years_left > 0:
        print(f'Years left for retirement for {name}: {retirement_years_left} years')
    else:
        print('You are already retired')

yearsToRetirement(1965, 'Mustafa')

print(help(yearsToRetirement))
