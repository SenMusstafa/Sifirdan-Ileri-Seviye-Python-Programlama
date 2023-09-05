#1: Find the numerical values in the list elements.
my_list = ["1", "2", "5a", "10b", "abc", "10", "50"]
for x in my_list:
    try:
        result = int(x)
        print(result)
    except ValueError:
        continue

#2: Ensure that the input is a number until the user enters 'q', 
# otherwise, display an error message.
while True:
    num = input('Enter a number: ')
    if num == 'q':
        break
    try:
        result = float(num)
        print('You entered a number: ', result)
    except ValueError:
        print('Invalid number')
        continue

#3: Generate an error for passwords containing Turkish characters.
def check_password(psw):
    import re
    if re.search("[ğ, Ğ, ş, Ş, ı, İ, Ç, ç, Ü, ü, Ö, ö]", psw):
        raise Exception("Password cannot contain Turkish characters")
    else:
        print("Valid password :)")

password = input("Enter a password: ")
try:
    check_password(password)
except Exception as ex:
    print(ex)

#4: Create a factorial function and provide error messages for input values.
def factorial(x):
    x = int(x)

    if x < 0:
        raise ValueError('Negative value')
    
    result = 1

    for i in range(1, (x + 1)):
        result *= i
    return result

for x in [5, 10, 20, -3, '10a']:
    try:
        y = factorial(x)
    except ValueError as err:
        print(err)
        continue
    print(y)
