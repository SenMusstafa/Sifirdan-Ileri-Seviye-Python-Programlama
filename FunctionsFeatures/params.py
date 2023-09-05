def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Division by zero error"
    return a / b

def perform_operation(func, a, b):
    return func(a, b)

def operation(func1, func2, func3, func4, operation_name):
    if operation_name == "addition":
        print(func1(2, 3))

    elif operation_name == "subtraction":
        print(func2(8, 3))

    elif operation_name == "multiplication":
        print(func3(5, 4))

    elif operation_name == "division":
        print(func4(50, 5))

    else:
        print("Invalid operation")

operation(addition, subtraction, multiplication, division, "addition")
operation(addition, subtraction, multiplication, division, "subtraction")
operation(addition, subtraction, multiplication, division, "multiplication")
operation(addition, subtraction, multiplication, division, "division")
