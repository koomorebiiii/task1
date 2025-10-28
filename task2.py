from typing import Callable, List, Optional, Any

def apply_filter(predicate: Callable[[Any], bool], items: Optional[List[Any]]) -> List[Any]:
    if items is None:
        return []
    
    if not callable(predicate):
        raise TypeError("Параметр predicate должен быть вызываемым")
    
    return list(filter(predicate, items))

# Тестовый массив для демонстрации
test_array = [
    "apple", "banana", "  orange juice", "avocado toast", "pear",
    "apricot", "grape", "kiwi", "mango", "ananas", "apple pie"
]

# Фильтрация строк с пробелами
no_spaces = apply_filter(lambda x: ' ' not in x, test_array)
print("Исключить строки с пробелами:", no_spaces)

# Фильтрация строк, начинающихся с 'a'
no_a_start = apply_filter(lambda x: not x.startswith('a'), test_array)
print("Исключить строки, начинающиеся с 'a':", no_a_start)

# Фильтрация строк длиной меньше 5
min_length_5 = apply_filter(lambda x: len(x) >= 5, test_array)
print("Исключить строки длиной меньше 5:", min_length_5)