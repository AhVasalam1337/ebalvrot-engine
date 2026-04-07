using System;

namespace EbalvrotEngine
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("--- Ebalvrot C# Engine: Калькулятор v1.0 ---");
            try
            {
                Console.Write("Введите первое число: ");
                double num1 = Convert.ToDouble(Console.ReadLine());

                Console.Write("Введите операцию (+, -, *, /): ");
                string op = Console.ReadLine();

                Console.Write("Введите второе число: ");
                double num2 = Convert.ToDouble(Console.ReadLine());

                double result = 0;

                switch (op)
                {
                    case "+": result = num1 + num2; break;
                    case "-": result = num1 - num2; break;
                    case "*": result = num1 * num2; break;
                    case "/": 
                        if (num2 != 0) result = num1 / num2; 
                        else { Console.WriteLine("Ошибка: деление на ноль"); return; }
                        break;
                    default: Console.WriteLine("Неверная операция"); return;
                }

                Console.WriteLine($"Результат: {result}");
            }
            catch (FormatException)
            {
                Console.WriteLine("Ошибка: введите корректные числа.");
            }
        }
    }
}