from MyModule import *

current_user = []

while True:
    if len(current_user) != 0:
        print(f"Tere tulemast, {current_user[0].get('user_name')}!")
    else:
        print(f"Tere tulemast, kasutaja!")
    sleep(1)
    print("+-------------Menu-------------+")
    print(
        "'0' - Registreerimine\n'1' - Autoriseerimine\n'2' - Parooli või nime muutmine\n'3' - Unustatud salasõna "
        "taastamine\n'4' - Teavet minu kohta\n'5' - Logi välja")
    print("+------------------------------+\n")
    try:
        v = int(input("Mida te tahate? "))
    except:
        continue

    if v == 0:
        if len(current_user) == 0:
            nimi = VariableCheck("Mis sinu nimi on? ", 'See nimi on juba olemas.', FindUserByName, find_user_condition=True)
            password = MakePassword()
            new_user = Registration(nimi, password)

            secret_word = input("Mõtle välja salajane sõna! ")
            new_user["secret_word"] = secret_word
            v = VariableCheck("Kas soovite posti lisada? ", "Vale vastus", AnswerConverter)
            if v is True:
                email = input("Mis post see on? ")
                new_user['email'] = email
            user_data.append(new_user)
            current_user.append(new_user)
        else:
            print("Te olete juba olemas! \n")
    elif v == 1:
        if len(current_user) == 0:
            name = input("Kirjutage oma nimi! ")
            password = input("Kirjuta oma parool! ")
            log_user = Authorization(name, password)
            if not log_user:
                print("ei ole õige nimi või parool!")
            else:
                current_user.append(log_user)
        else:
            print("Te olete juba olemas! \n")
    elif v == 2:
        if len(current_user) != 0:
            v = VariableCheck("Mida soovite muuta, nime(1) või parooli(0)? ", "Vale vastus!", AnswerConverter)
            if v:
                new_user_name = VariableCheck("Mis on uus nimi? ", "See nimi on juba hõivatud.", FindUserByName, find_user_condition=True)
                current_user[0]['user_name'] = new_user_name
                ChangeValueOfUserData(current_user[0].get("user_id"), "user_name", new_user_name)
            else:
                new_user_password = MakePassword()
                current_user[0]['user_password'] = new_user_password
                ChangeValueOfUserData(current_user[0].get("user_id"), "user_password", new_user_password)

        else:
            print("Nime või parooli muutmiseks peate olema registreeritud! ")
    elif v == 3:
        if len(current_user) == 0:
            print("Kuidas soovite parooli sisestada?\n(0) - Salajane sõna\n(1) - Post\n")
            v = VariableCheck("Kuidas sa seda teha tahad? ", "vale vastus!", AnswerConverter)
            if v:
                user = VariableCheck("Kirjutage oma e-post: ", "Sellist e-post ei ole olemas! ", FindUserByEmail)
                if user != 'EXIT':
                    email = user.get("email")
                    code = SendMail(email)
                    print("Teie e-postile tuli kood")
                    while True:
                        input_code = input("Kood: ")
                        if CheckEmailCode(email, input_code) or InputQuit(input_code):
                            break
                        print("See pole õige kood!")

                    if not InputQuit(input_code):
                        if input_code == code:
                            user = FindUserByEmail(email)
                            current_user.append(user)
            else:
                user = VariableCheck("Palun kirjutage oma nimi: ", "Sellist nime ei ole olemas! ", FindUserByName)
                secret_word = input("Sisesta oma salajane sõna: ")
                if not InputQuit(secret_word):
                    if secret_word == user.get("secret_word"):
                        current_user.append(user)
                    else:
                        print('Salasõna ei ole õige!')
        else:
            print("Te olete juba registreeritud!")
    elif v == 4:
        if len(current_user) != 0:
            InformationDisplay(current_user[0])
        else:
            print("Sa pead end registreerima, et alustada!")
    elif v == 5:
        if len(current_user) != 0:
            current_user.clear()
            print("Te olete kontolt väljas!\n")
            sleep(1)
        else:
            print("Sa pead end registreerima, et alustada!")
    elif v == 6:
        print(user_data)
    elif v == 404:
        break
    else:
        print("Selline tähendus ei ole oluline.")
        sleep(1)
