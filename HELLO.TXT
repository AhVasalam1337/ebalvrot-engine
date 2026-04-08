def calculate_shit_index(input_value):
    """
    Рассчитывает метафизический артефакт в каловых единицах.
    Формула: (значение * коэффициент_шаурмы) / бренность_бытия
    """
    constant_shawarma = 13.37
    life_futility = 0.42
    
    result = (float(input_value) * constant_shawarma) / life_futility
    return round(result, 2)

if __name__ == "__main__":
    print("> [SYSTEM]: Ebalvrot Engine Shit-Calculator v1.0")
    try:
        val = input("> Введите массу метафизического объекта: ")
        print(f"> Результат анализа: {calculate_shit_index(val)} кг какашек.")
        print("> Вывод: всё превращается в какашки. Даже твой код.")
    except Exception as e:
        print("> Ошибка: объект слишком материален для этого мира.")