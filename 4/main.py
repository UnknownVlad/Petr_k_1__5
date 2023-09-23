import re

def reverse_words(text):
    words = re.findall(r'\w+', text)  # Ищем все слова в тексте
    result = []
    for word in words:
        reversed_word = word[::-1]  # Переворачиваем каждое слово
        result.append(reversed_word)
    # Заменяем слова в исходном тексте на перевернутые слова
    encoded_text = re.sub(r'\w+', lambda m: result.pop(0), text)
    return encoded_text

text = "Помимо C# вы будете изучать Java, C++ и другие языки программирования."
encoded_text = reverse_words(text)
print(encoded_text)