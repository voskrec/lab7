#делаем функцию которая убирает лишние знаки
#так же проверяет на панлиндром
def palindrome(text):
    text=text.lower().replace(" ","").replace(",","").replace("?","").replace("!","")
    return text==text[::-1]
text=input("введите текст:")
#проверяем является ли введённый текст палиндромом
if palindrome(text):
    print("палиндром")
else:
    print("не палиндром")