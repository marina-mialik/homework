"""
Написать функцию (без регулярных выражений), которая принимает текстовую строку 
и возвращает словарь, который содержит информацию о количестве 
символов, слов, строк и предложений в тексте. 
Затем создайте вторую функцию, которая принимает этот словарь, 
и выводит его содержимое в удобном и красивом формате. 

"""
CHARS = 'chars'
WORDS = 'words'
STRINGS = 'strings'
SENTENCES = 'sentences'

def info_data(data: str) -> dict:
    hash = {}
    hash[CHARS] = len(data)
    hash[WORDS] = len(data.split())
    hash[STRINGS] = len(data.splitlines())

    sentence = 0
    for char in data:
        if char in ".!?":
            sentence += 1

    hash[SENTENCES] = sentence

    return hash

def get_data(hash: dict) -> dict:
    names = {}
    names[CHARS] = 'Символы'
    names[WORDS] = 'Слова'
    names[STRINGS] = 'Строки'
    names[SENTENCES] = 'Предложения'

    print("Информация по тексту:")
    print("------------------")
    for key in hash.keys():
        print(names[key], hash[key])
    print("------------------")

data = info_data("""
Колядую, колядую
Я зайду в избу любую.
Попрошу хозяйку
Сладостей давай-ка.
И печенья, и конфет,
И с орехами щербет,
И халву, и шоколад,
Пастилу и мармелад,
Вкусное пирожное,
Сладкое мороженое!
Мы и сами будем есть
И друг друга угощать
А хозяйку, а хозяйку
Добрым словом поминать!
""".strip())

get_data(data)
