import re
def count(text:str)->int:
    words = re.findall(r'\b\w+\b',text)
    return len(words)
text=input("введите текст:")
print(f'колличесвто слов:{count(text)}')