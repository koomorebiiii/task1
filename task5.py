import time
from typing import Callable, Any, List

def timer(func: Callable) -> Callable:
    def wrapper(*args, **kwargs) -> Any:
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        
        execution_time = end_time - start_time
        print(f"Функция '{func.__name__}' выполнилась за {execution_time:.6f} секунд")
        return result
    return wrapper

def read_numbers_from_file(filename: str) -> List[int]:
    with open(filename, 'r', encoding='utf-8') as f:
        return [int(line.strip()) for line in f if line.strip()]

def write_result_to_file(filename: str, a: int, b: int, result: int) -> None:
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"Сумма {a} + {b} = {result}")

@timer
def sum_numbers(a: int, b: int) -> int:
    result = a + b
    print(f"Сумма {a} + {b} = {result}")
    return result

@timer
def process_file(
    input_file: str = "input.txt", 
    output_file: str = "output.txt",
    numbers_required: int = 2) -> None:
    try:
        # Чтение
        numbers = read_numbers_from_file(input_file)
        
        # Валидация
        if len(numbers) < numbers_required:
            raise ValueError(f"Файл должен содержать как минимум {numbers_required} чисел")
        
        # Операция
        a, b = numbers[0], numbers[1]
        result = sum_numbers(a, b)
        
        # Запись
        write_result_to_file(output_file, a, b, result)
        print(f"Результат записан в файл '{output_file}'")
    
    except FileNotFoundError:
        print(f"Ошибка: файл '{input_file}' не найден")
    except ValueError as e:
        print(f"Ошибка данных: {e}")

def main():
    print(" ТЕСТИРОВАНИЕ ДЕКОРАТОРА ")
    
    # Тест 1:
    print("\n1. Сумма чисел:")
    sum_numbers(1055677657, 2598766454)
    
    # Тест 2: Обработка существующего файла
    print("\n2. Тест обработки файлов:")
    process_file()
    
    # Тест 3: Ошибка файла
    print("\n3. Тест обработки ошибок:")
    process_file("nonexistent.txt", "output.txt")

if __name__ == "__main__":
    main()