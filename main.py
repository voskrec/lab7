def caesar_cipher(text: str, shift: int) -> str:
    """Шифрует текст шифром Цезаря (сдвигает буквы по алфавиту)."""
    
    # Список для символов (склеим в строку в конце — так быстрее)
    result = []
    
    for char in text:
        if char.isalpha():
            # Определяем базу: код 'A' для заглавных, код 'a' для строчных
            base = ord('A') if char.isupper() else ord('a')
            
            # Формула: позиция в алфавите + сдвиг, % 26 зацикливает алфавит
            shifted = (ord(char) - base + shift) % 26 + base
            
            result.append(chr(shifted))
        else:
            # Знаки препинания, пробелы и цифры оставляем без изменений
            result.append(char)
            
    return "".join(result)


# --- Тестирование ---
original = "Hello, World!"
encrypted = caesar_cipher(original, 3)
print(f"Оригинал: {original}")
print(f"Зашифровано: {encrypted}")  # Khoor, Zruog!

# Для расшифровки просто передаем отрицательный сдвиг
decrypted = caesar_cipher(encrypted, -3)
print(f"Расшифровано: {decrypted}") # Hello, World!