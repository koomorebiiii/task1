def is_palindrome(string_to_check):
    cleaned_string = ''.join(char.lower() for char in string_to_check if char.isalnum())
    left_index = 0
    right_index = len(cleaned_string) - 1

    while left_index < right_index:
        if cleaned_string[left_index] != cleaned_string[right_index]:
            return False
        left_index += 1
        right_index -= 1

    return True

test_strings = [
    "r", "", "Was it a car or a cat I saw?",
    "No 'x' in Nixon", "Hello, World!", "level up"
]

print("Результаты:")
for test_str in test_strings:
    result = is_palindrome(test_str)
    print(f"'{test_str}' -> {result}")