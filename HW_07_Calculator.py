# Task 1 - Calculator

def calculator():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Choose an operation (Enter +, -, *, / or ^): ")

        if operation == '+':
            print("You chose addition")
            result = num1 + num2
        elif operation == '-':
            print("You chose subtraction")
            result = num1 - num2
        elif operation == '*':
            print("You chose multiplication")
            result = num1 * num2
        elif operation == '/':
            print("You chose division")
            if num2 == 0:
                print("Error: division by zero!")
                result = None
            else:
                result = num1 / num2
        elif operation == '^':
            print("You chose square")
            result = num1 ** 2
        else:
            print("Invalid operation!")
            result = None

        print("Result:", result)

    except ValueError:
        print("Error: please enter valid numbers!")

calculator()