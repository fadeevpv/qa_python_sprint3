
import random
user_name = 'fadeev_qa_python_06_'
user_domen = '@ya.ru'
name = 'fadeev'

def user_login_generator():
    user_email = user_name + str(random.randint(100, 999)) + user_domen

    return user_email

def user_password_generator():
    user_password = random.randint(1000000, 9999999)

    return user_password


def user_lastname_generator():
    last_name = name + str(random.randint(100, 999))
    return last_name





