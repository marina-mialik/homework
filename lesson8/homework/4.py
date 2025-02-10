'''

Написать функцию, которая возвращает любое число в виде денежной величины 
с разделителями групп разрядов в качестве пробела и валютой в конце. 
Денежная величина всегда должна содержать количество копеек в виде дух 
знаков после точки, даже если исходное число целое. 
*Нельзя использовать форматную строку.
Например: 1234567 -> "1 234 567.00 руб."

с помощью try перехватить возможные ошибки.
'''

def get_currency(amount: float) -> str:
    try:
        if not isinstance(amount, (int, float)):
            raise ValueError("Переданное значение должно быть числом")
        
        currency, cents = "{:.2f}".format(amount).split(".")
        currency = " ".join(currency[::-1][i:i+3] for i in range(0, len(currency), 3))
        currency = currency[::-1]

        return "{}.{} руб.".format(currency, cents)
    except Exception as e:
        return "Ошибка: {}".format(e)

print(get_currency(1234567))     
print(get_currency(1234567.9))   
print(get_currency(1234567.123))              
print(get_currency("abcd"))   
