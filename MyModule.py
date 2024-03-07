from ModuleImports import *
symbols_list = [string.octdigits, string.ascii_letters, string.punctuation]

def InputQuit(value):
    quit_words = ['QUIT','404','BREAK','EXIT','LÕPETADA','LÕPP','КОНЕЦ']
    if any(i in value.upper() for i in quit_words):
        return True
    return False
def VariableCheck(input_text, false_text, func, find_user_condition = False): # очень-очень часто появлялся код который написан снизу, поэтому пришлось сделать функцию
    if find_user_condition:
        find_user = not None
        while find_user is not None:
            variable = input(input_text)
            if InputQuit(variable):
                return 'EXIT'
            find_user = func(variable)
            if func(variable) is not None:
                print(false_text)
                sleep(1)
    else:
        variable = None
        while variable is None:
            variable = input(input_text)
            if InputQuit(variable):
                return 'EXIT'
            variable = func(variable)
            if variable is None:
                print(false_text)
                sleep(1)
    return variable

def ChangeValueOfUserData(user_id, variable, value):
    user_data[user_id][variable] = value

def AnswerConverter(answer = None, make_question = True):
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

def NameCheck(name:str):
    return False

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
    return True, 'success'

def MakePassword(random_password = None, choice = True):
    if choice:
        random_password = VariableCheck("Kas soovite parooli geniseerida või ise välja mõelda? ", "Vale vastus", AnswerConverter)
    password = None
    if random_password:
        password = PasswordGeneration()
    else:
        while True:
            password = input("Mõtle välja parool: ")
            success, message = PasswordCheck(password)
            if success:
                return password
            else:
                print(message)
    return password

def FindUserByValue(value, get_value):
    for user in user_data:
        if value == user.get(get_value):
            return user
    return None

def FindUserByEmail(email):
    return FindUserByValue(email, "email")


def FindUserByName(name):
    return FindUserByValue(name, "user_name")

def CheckEmailCode(email, code):
    for email_code in email_data:
        if code == email_code.get("code") and email == email_code.get('email'):
            return True
    return False

def Registration(name: str, password:str, user_return=True, max_id_return=False):
    user = {
        "user_id": len(user_data),
        "user_name": name,
        "user_password": password
    }

    return_tuple = list()
    if user_return:
        return_tuple.append(user)
    if max_id_return:
        return_tuple.append(len(user_data))
    return tuple(return_tuple) if len(return_tuple) > 1 else return_tuple[0]

def Authorization(name, password):
    user = FindUserByName(name)
    if user is None:
        return False
    if password != user.get("user_password"):
        return False
    return user

def CodeGenerator():
    letters_numbers_list = [string.ascii_letters, string.digits]
    code = str()
    for _ in range(0, randint(5, 9)):
        random_symbol_lst_index = randint(0, 1)
        code += str(
            letters_numbers_list[random_symbol_lst_index][randint(0, len(letters_numbers_list[random_symbol_lst_index]) - 1)])
    return code

def SendMail(email):
    file = "email.txt"
    code = CodeGenerator()
    email_data.append({'email':email,'code':code})
    with open(file, mode="w", encoding="utf-8") as f:
        f.write(f"{email} - {code}")
    return code

def InformationDisplay(user):
    print("+-------------------------+")
    print(f"Nimi - '{user.get('user_name')}'\nPassword - '{user.get('user_password')}'\nSecret word - '{user.get('secret_word')}'\n{'Email - ' + user.get('email') if 'email' in user else ''}")
    print("+-------------------------+\n")
