'''
Запросить фразу состоящую минимум из трех слов. 
Сформировать фразу из этих слов в которой каждая буква слова, 
продублирована то количество раз, которое соответствует номеру позиции 
данной буквы в слове этой буквы. 
Например: Привет как дела => Прриииввввееееетттттт кааккк деелллаааа

'''

phrase = input()
words = phrase.split()
result = []

for word in words:
    new_word = ""
    for i, letter in enumerate(word):
        new_word += letter * (i + 1)
    result.append(new_word)

print(*result)