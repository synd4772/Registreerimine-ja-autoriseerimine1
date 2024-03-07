import string
from random import *
from UserData import *

symbols_list = [string.octdigits, string.ascii_letters, string.punctuation]

def AnswerConverter(answer):
    t_ans = ['JAH', '1', 'YES', 'ДА']
    f_ans = ['EI', '0', 'NO', 'НЕТ']
    if any(i in answer.upper() for i in t_ans):
        return True
    elif any(i in answer.upper() for i in f_ans):
        return False
    else:
        return None


# if any(i in answer.upper() for i in t_ans): return True
# то что сверху эквивалентно тому, что снизу.
# return True if any(i in answer.upper() for i in t_ans) else False
# метод any проверяет есть ли хотя бы один элемент в
def MakePassword(random_password: bool):
    password = None

    if random_password:
        password = PasswordGeneration()
    else:
        password = input("Mõtle välja parool: ")

    return password


def PasswordGeneration():
    password = str()
    for _ in range(0, randint(5, 9)):
        random_symbol_lst_index = randint(0, 2)
        password += str(symbols_list[random_symbol_lst_index][randint(0, len(symbols_list[random_symbol_lst_index]) - 1)])
    return password

def PasswordCheck(password: str):
    if len(password) < 5:
        return False, "Paroolil peab olema vähemalt 5 tähemärki"
    for symbol_list in symbols_list:
        for symbol in symbol_list:
            if list(password).count(symbol) == len(password):
                return False, "Parool ei tohi koosneda samadest sümbolitest"
    maybe_password = ""
    for number in range(0, 20):
        maybe_password += str(number)
        if password == maybe_password or password == maybe_password[1:-1]:
            return False, "Keerulisemad salasõnad"
    return True, "success"


def FindUser(name):
    for user in user_data:
        if name == user.get("user_name"):
            return user
    return None


def Registration(name: str, password=PasswordGeneration(), user_return=True, max_id_return=False):
    if FindUser(name) is None:
        return False
    user = {
        "user_id": len(user_data) + 1,
        "user_name": name,
        "user_password": password
    }

    return_tuple = list()
    if user_return:
        return_tuple.append(user)
    if max_id_return:
        len(user_data)
    return tuple(return_tuple)


def Authorization(name, password):
    user = FindUser(name)
    if user is None:
        return False
    if password != user.get("user_password"):
        return False
    return user
