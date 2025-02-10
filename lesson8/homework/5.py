'''
Написать функцию count_char, которая принимает строковое значение,
из которого создает и возвращает словарь, следующего вида:
{'буква': 'количество-вхождений-в-строку'}
Нельзя пользоваться collections.Counter!

'''

def count_char(word: str) -> dict:
    hash = {}

    for char in word:
        hash[char] = hash.get(char, 0) + 1

    return hash    

print(count_char("word"))  
print(count_char("aaaabbbbddoaat"))  
print(count_char("12345"))
print(count_char(""))  