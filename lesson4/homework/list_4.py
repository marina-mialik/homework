'''
Дан список:
['hello', 'python', 'интерпретатор', 'pep8', "123"]
Вернуть список где вместо элементов данного списка прописаны количество символов каждого элемента.

'''

my_list = ['hello', 'python', 'интерпретатор', 'pep8', "123"]

words_length = [len(item) for item in my_list]

print(words_length)