def calculator():
    try:
        # Вводим два числа и операцию от пользователя
        number_1 = float(input("Введите первое число: "))
        number_2 = float(input("Введите второе число: "))
        operation = input("Введите операцию: ")

        def handle_calculation_error():
            # Возвращает "Undefined" при попытке деления на 0 или операциях с 0, в противном случае "Деление на 0 запрещено"
            return "Undefined" if not number_1 and not number_2 and operation in ('/', '%', '//') else "Деление на 0 запрещено"

        # Словарь операций, где ключ - операция, значение - лямбда-функция, выполняющая соответствующую операцию
        operations = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: x / y if y != 0 else handle_calculation_error(),
            "%": lambda x, y: x % y if x != 0 and y != 0 else handle_calculation_error(),
            "**": lambda x, y: x ** y,
            "//": lambda x, y: x // y if y != 0 else handle_calculation_error(),
        }

        # Получаем результат выполнения операции или сообщение об ошибке, если операция не поддерживается
        result = operations.get(operation, lambda x, y: f"Операция {operation} не поддерживается")(number_1, number_2)

        # Выводим результат
        print(result)

    except ValueError as e:
        # Обработка ошибки ввода (введено не число)
        print(f"Ошибка ввода: {e}")

# Вызываем функцию калькулятора
calculator()