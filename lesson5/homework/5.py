"""
Запросить фразу 
    - вывести на экран количество уникальных символов
    - вывести на экран количество уникальных слов
    -* вывести символ который встречался чаще всего

"""

phrase = input("Введите фразу: ")

unique_chars = set(phrase.lower())
print(f"Количество уникальных символов: {len(unique_chars)}")

words = phrase.lower().split()
unique_words = set(words)
print(f"Количество уникальных слов: {len(unique_words)}")

char_dict = {}
most_popular_char = ""

for char in phrase.lower():
  char_dict[char] = char_dict.get(char, 0) + 1
  
  if char_dict[char] > char_dict.get(most_popular_char, 0):
    most_popular_char = char

# В случае если у нас несколько символов имеют одинаковое самое большое вхождение во фразу
# for key in char_dict.keys():
#   if char_dict[key] == char_dict[most_popular_char]:
#     print(key, end=" ")
# print()

print(f"Самый частый символ: {most_popular_char}")
