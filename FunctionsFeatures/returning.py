def calculator(operation_name):
    def addition(*args):
        total = 0
        for num in args:
            total += num
        return total

    def multiplication(*args):
        product = 1
        for num in args:
            product *= num
        return product

    if operation_name == "addition":
        return addition
    elif operation_name == "multiplication":
        return multiplication
    else:
        raise ValueError("Invalid operation name")

addition = calculator("addition")
print(addition(1, 3, 5, 7, 9))

multiplication = calculator("multiplication")
print(multiplication(3, 5))
