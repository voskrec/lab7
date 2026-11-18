import re

def validate_email(email: str) -> bool:
    """Проверяет корректность email."""
    # ^[\w.-]+@[\w.-]+\.\w+$ — имя_пользователя@домен.зона
    pattern = r'^[\w.-]+@[\w.-]+\.\w+$'
    return bool(re.match(pattern, email))


def validate_phone(phone: str) -> bool:
    """Проверяет корректность российского телефона."""
    # Допускает формат: +7 (999) 123-45-67 (пробелы, скобки и дефисы необязательны)
    pattern = r'^\+?7[\s-]?\(?\d{3}\)?[\s-]?\d{3}[\s-]?\d{2}[\s-]?\d{2}$'
    return bool(re.match(pattern, phone))


def validate_url(url: str) -> bool:
    """Проверяет корректность URL."""
    # Строка должна начинаться с http:// или https:// и содержать домен
    pattern = r'^https?:\/\/[\w.-]+[a-z]{2,}(\/[\w.-]*)*$'
    return bool(re.match(pattern, url))


# --- Тестирование ---
# Кортежи: (тип, проверяемое значение, функция-валидатор)
tests = [
    ("email", "ivan@example.com", validate_email),
    ("email", "invalid@", validate_email),
    ("phone", "+7 (999) 123-45-67", validate_phone),
    ("url", "https://example.com", validate_url),
    ("url", "not-a-url", validate_url),
]

for type_, value, validator in tests:
    # Выводим ✓ при успехе и ✗ при ошибке
    result = "✓" if validator(value) else "✗"
    print(f"{result} {type_}: {value}")