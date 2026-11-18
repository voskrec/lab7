def count_letters(text: str) -> tuple:
    # Создаем множества (set) для быстрого поиска.
    # Используем русские и английские буквы в нижнем регистре.
    vowels = set("аеёиоуыэюяaeiouy")
    consonants = set("бвгджзйклмнпрстфхцчшщbcdfghjklmnpqrstvwxz")
    
    # Счетчики
    vowel = 0
    consonant= 0
    
    # Проходим по каждому символу в тексте
    for char in text.lower():  # .lower() приводит всё к нижнему регистру
        if char in vowels:
            vowel_count += 1
        elif char in consonants:
            consonant_count += 1
            
    return vowel, consonant

# --- Использование ---
user_text = input("Введите текст: ")
vowels, consonants = count_letters(user_text)

print(f"Гласных: {vowels}")
print(f"Согласных: {consonants}")