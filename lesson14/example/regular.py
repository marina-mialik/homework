# match - только с начала строки .group(0)
# search - везде - возвращает только 1
# findall - список всего
# split - разделить 
# sub - замена 
# compile - делает объект 
# 	pattern = re.compile('AV') / 
# 	patern.findall(text
# 	)


# {} - сколько
# [] - какаие символы [a-zA-Z,.!@]
# + - 1 или больше
# * - 0 или больше
# ? - одно повторение
# () одно из обязательных условий
# . - любой символ
# ^ - начало
# $ - окончание строки
 
# \b - границы слова
# \d — соответствует любой одной цифре и заменяет собой выражение [0-9];
# \D — исключает все цифры и заменяет [^0-9];
# \w — заменяет любую цифру, букву, а также знак нижнего подчёркивания;
# \W — любой символ кроме латиницы, цифр или нижнего подчёркивания;
# \s — соответствует любому пробельному символу;
# \S — описывает любой непробельный символ.


	# '^\w+' - первое слово
	# ^[a-zA-Z][a-zA-Z0-9-_\.]{1,20}$ - логин
	# ^(?=.*[0-9].*)(?=.*[a-z].*)(?=.*[A-Z].*)[0-9a-zA-Z]{8,}$ - пароль
	# (?=^.{8,}$)((?=.*\d)|(?=.*\W+))(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$ - пароль более 8 символов
	# (\+375)(29|33|44)[0-9]{7}
	# \d\d\/\d\d\/\d{4}
	# [-+]?\d+ = +12121 -6546
 
 
import re
s = '3752912345678'

res = re.search(r'\+*375(29|33|44)[0-9]{7}', s)

if res:
	print(res[0])
	print(res.group(0))


# s='175/65R14 Кама Euro 129, 82H 175/65/R14 Кама Euro 129, 82H'
# res = re.findall(r'\d{3}\/\d{2}\/*R\d{2}', s)
# print(res[0] if res else None)