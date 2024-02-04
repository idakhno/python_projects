"""
calculator.py

Simple calculator module for basic arithmetic operations.
Takes two numbers and an operation as input, then prints the result.

Usage:
1. Run the module, and enter the first number, second number, and operation.
2. Supports addition (+), subtraction (-), multiplication (*), division (/),
   modulo (%), exponentiation (**), and floor division (//).

Example:
Enter the first number: 10
Enter the second number: 5
Enter the operation: +
Output: 15
"""


def handle_calculation_error(number_1, number_2, operation):
    """
    Handles calculation errors based on the provided numbers and operation.

    Returns an error message if the calculation is undefined
    or involves division by zero.

    :param number_1: The first number.
    :param number_2: The second number.
    :param operation: The arithmetic operation.
    :return: Error message or "Undefined" based on the calculation.
    """
    return (
        "Undefined"
        if not (number_1 and number_2) and operation in ("/", "%", "//")
        else "Division by 0 is prohibited"
    )


def perform_operation(number_1, number_2, operation):
    """
    Performs the specified arithmetic operation on the provided numbers.

    :param number_1: The first number.
    :param number_2: The second number.
    :param operation: The arithmetic operation.
    :return: Result of the operation or an error message.
    """

    def handle_condition(x, y, operation):
        """Handles arithmetic operations avoiding division by zero."""
        if x != 0 and y != 0:
            return operations[operation](x, y)
        else:
            return handle_calculation_error(number_1, number_2, operation)

    operations = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: handle_condition(x, y, "/"),
        "%": lambda x, y: handle_condition(x, y, "%"),
        "**": lambda x, y: x ** y,
        "//": lambda x, y: handle_condition(x, y, "//"),
    }

    return operations.get(
        operation, lambda x, y: f"Operation {operation} is not supported"
    )(number_1, number_2)


def calculate():
    """
    Performs basic arithmetic calculations based on user input.

    Prompts the user to enter two numbers and an operation.
    Supports addition (+), subtraction (-), multiplication (*), division (/),
    modulo (%), exponentiation (**), and floor division (//).
    Prints the result of the calculation.
    """
    try:
        number_1 = float(input("Enter the first number: "))
        number_2 = float(input("Enter the second number: "))
        operation = input("Enter the operation: ")

        result = perform_operation(number_1, number_2, operation)

        print(result)

    except ValueError as e:
        print(f"Input error: {e}")


calculate()
