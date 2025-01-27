'''
Дана строка - "Это тестовая <start>строка для изучения<end> строковых операций". 
Программа должна вывести на экран текст из данной строки     
заключенный между тэгами <start> и <end>. 
Программа должна работать с любой другой строкой с подобными тэгами.

'''

s = "Это тестовая <start>строка для изучения<end> строковых операций"

start_mark = '<start>'
end_mark = '<end>'

start_index = s.find(start_mark) + len(start_mark)
end_index = s.find(end_mark)

print(s[start_index:end_index])