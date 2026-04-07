import math

def advanced_calculator():
    print("--- Ebalvrot Advanced Engine: Калькулятор v2.0 ---")
    try:
        num1 = float(input("Введите число: "))
        op = input("Введите операцию (+, -, *, /, ^, sqrt): ")

        if op == 'sqrt':
            result = math.sqrt(num1) if num1 >= 0 else "Ошибка: корень из отрицательного числа"
        else:
            num2 = float(input("Введите второе число: "))
            if op == '+': result = num1 + num2
            elif op == '-': result = num1 - num2
            elif op == '*': result = num1 * num2
            elif op == '/': result = num1 / num2 if num2 != 0 else "Ошибка: деление на ноль"
            elif op == '^': result = math.pow(num1, num2)
            else: result = "Неверная операция"
        
        print(f"Результат: {result}")
    except ValueError:
        print("Ошибка: введите корректные данные.")

if __name__ == "__main__":
    advanced_calculator()