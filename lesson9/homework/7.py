"""
Дан список пользователей след. формата: 
[{"name":"some_name", "login":"some_login", "password":"some_password" },
 ...
]

Отфильтровать используя функцию filter() список на предмет паролей 
которые менее 5 символов.

*Отфильтровать используя функцию filter() список на предмет валидных логинов. 
Валидный логин должен содержать только латинские буквы, цифры и черту подчеркивания. 
Каждому пользователю с плохим логином вывести текст 
"Уважаемый user_name, ваш логин user_login не является корректным."

"""
import string

credentials = [
    { "name":"some_name", "login":"some_login", "password":"some_password" },
    { "name": "Emma Wilson", "login": "emma_w", "password": "EmW!l$0n2023" },
    { "name": "Liam Johnson", "login": "liam_j", "password": "Lj0h" },
    { "name": "Olivia Brown", "login": "olivia.b", "password": "0Br0wn!Pass" },
    { "name": "Noah-Smith", "login": "n.smith", "password": "N03" },
    { "name": "Ava Davis", "login": "a.davis", "password": "D@v!sAva_987" },
    { "name": "Alice-Johnson", "login": "alicej", "password": "AJ!2023" },
    { "name": "Bob Smith", "login": "bsmith", "password": "B0bSmi7h" },
    { "name": "Carol Taylor", "login": "carol_t", "password": "Ct#2023 "},
    { "name": "Иван Иванов", "login": "ivan_i", "password": "Ив" },
    { "name": "Мария Петрова", "login": "maria.p", "password": "М@рия_Петр0ва" },
    { "name": "Алексей Сидоров", "login": "a.sidorov", "password": "S!d0r0v_123" },
    { "name": "Екатерина Кузнецова", "login": "ekaterina_k", "password": "Кузнец0в@Ек!" },
    { "name": "Дмитрий Смирнов", "login": "dmitry_s", "password": "Смм#" }
]

filter_credentials = list(filter(lambda credential: len(credential["password"]) < 5, credentials))
print("Список пользователей у которых пароль меньше 5:")
[print(user) for user in filter_credentials]


def is_valid_login(login):
    allowed_chars = string.ascii_letters + string.digits + "_"
    return all(char in allowed_chars for char in login)

def filter_valid_logins(users):
    invalid_users = list(filter(lambda user: not is_valid_login(user["login"]), users))

    for user in invalid_users:
        print(f"Уважаемый {user['name']}, ваш логин {user['login']} не является корректным.")

    valid_users = list(filter(lambda user: is_valid_login(user["login"]), users))
    return valid_users

valid_users = filter_valid_logins(credentials)

print("Список валидных реквизитов для входа:")
[print(user) for user in valid_users]
