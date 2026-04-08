def calculator():
    print("--- Ebalvrot Engine: Calculator ---")
    try:
        num1 = float(input("Введите первое число: "))
        op = input("Введите операцию (+, -, *, /): ")
        num2 = float(input("Введите второе число: "))

        if op == '+': result = num1 + num2
        elif op == '-': result = num1 - num2
        elif op == '*': result = num1 * num2
        elif op == '/': result = num1 / num2 if num2 != 0 else "Ошибка: деление на ноль"
        else: result = "Неверная операция"

        print(f"Результат: {result}")
    except ValueError:
        print("Ошибка: введите корректные числа.")

if __name__ == "__main__":
    calculator()