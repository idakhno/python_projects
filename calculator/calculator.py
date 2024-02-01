def calculator():
    try:
        # Input two numbers and an operation from the user
        number_1 = float(input("Enter the first number: "))
        number_2 = float(input("Enter the second number: "))
        operation = input("Enter the operation: ")

        def handle_calculation_error():
            # Returns "Undefined" when attempting division by 0 or operations involving 0; otherwise, returns "Division by 0 is prohibited"
            return "Undefined" if not number_1 and not number_2 and operation in ('/', '%', '//') else "Division by 0 is prohibited"

        # Dictionary of operations, where the key is the operation and the value is a lambda function performing the corresponding operation
        operations = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: x / y if y != 0 else handle_calculation_error(),
            "%": lambda x, y: x % y if x != 0 and y != 0 else handle_calculation_error(),
            "**": lambda x, y: x ** y,
            "//": lambda x, y: x // y if y != 0 else handle_calculation_error(),
        }

        # Get the result of the operation or an error message if the operation is not supported
        result = operations.get(operation, lambda x, y: f"Operation {operation} is not supported")(number_1, number_2)

        # Print the result
        print(result)

    except ValueError as e:
        # Handle input error (non-numeric input)
        print(f"Input error: {e}")

# Call the calculator function
calculator()