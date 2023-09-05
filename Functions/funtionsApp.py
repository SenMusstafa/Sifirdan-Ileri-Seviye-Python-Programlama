# 1- A function that displays a given word on the screen a specified number of times.
def show_word(word, count):
    print(word * count)
show_word('Merhaba\n', 10)

# 2- A function that converts any number of parameters into a list.
def convert_to_list(*params):
    return list(params)
result = convert_to_list(10, 20, 30, 'merhaba')
print(result)

# 3- A function that finds all prime numbers between two given numbers.
def find_prime_numbers(start, end):
    prime_numbers = []
    for num in range(start, end+1):
        if num > 1:
            is_prime = True
            for i in range(2, i + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                prime_numbers.append(num)
    return prime_numbers

start_num = int(input('Starting number: '))
end_num = int(input('Ending number: '))
prime_numbers = find_prime_numbers(start_num, end_num)
print('Prime numbers:', prime_numbers)


# 4- A function that returns a list of factors of a given number.
def find_factors(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

input_number = int(input("Enter a number: "))
factors_list = find_factors(input_number)
print("Factors:", factors_list)
