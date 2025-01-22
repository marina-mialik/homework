login = input("Введите логин: ")
password = input("Введите пароль: ")

is_login_correct = login == 'admin'
is_password_correct = password == '12345'

print(f"Логин: {is_login_correct} / Пароль: {is_password_correct}")