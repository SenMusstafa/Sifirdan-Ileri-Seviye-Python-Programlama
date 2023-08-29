numbers = [1, 3, 5, 9, 10, 4]

# Using the `map` function to apply a function to each element of a list.
def square(num):
    return num ** 2

def apply_square(numbers):
    return list(map(square, numbers))
squared_result = apply_square(numbers)
print("Squared using map and function:", squared_result)

# Using an anonymous (lambda) function with the `map` function.
def apply_square_lambda(numbers):
    return list(map(lambda num: num ** 2, numbers))
squared_lambda_result = apply_square_lambda(numbers)
print("Squared using map and lambda:", squared_lambda_result)

# Using the `filter` function to filter elements from a list.
def filter_even(numbers):
    return list(filter(lambda num: num % 2 == 0, numbers))
even_numbers = filter_even(numbers)
print("Even numbers using filter:", even_numbers)
