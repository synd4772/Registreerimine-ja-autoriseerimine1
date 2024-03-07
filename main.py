from MyModule import *
from time import *

user = []

while True:

    print("+-------------Menu-------------+")
    print("'0' - Registreerimine\n'1' - Autoriseerimine\n'2' - Parooli või nime muutmine\n'3' - Unustatud salasõna taastamine\n")
    print("+------------------------------+")
    try:
        v = int(input("Mida te tahate? "))
    except:
        pass
    if v == 0:
        if len(user) == 0:
            nimi = input("Mis su nimi on? ")
            while v is not True or v is not False:
                v = input("Kas soovite parooli geniseerida või ise välja mõelda? ")
                v = AnswerConverter(v)
                if v is None:
                    print("Vale vastus.")
                    sleep(2)
            password = MakePassword(v)

            if len(user) == 0:
                new_user = Registration(nimi, password)
                secret_word = input("Mõtle välja salajane sõna! ")
                new_user["secret_word"] = secret_word
                user_data.append(new_user)
                user.append(new_user)
        else:
            print("Te olete juba olemas! ")
    if v == 1:
        if len(user) == 0:
            name = input("Kirjutage oma nimi! ")
            password = input("Kirjuta oma parool! ")
            log_user = Authorization(name, password)
            if not log_user:
                print("ei ole õige nimi või parool!")
            else:
                user.append(log_user)
                print(f"Tere {user[0].get('user_name')}")
        else:
            print("Te olete juba olemas! ")
    if v == 2:
        if len(user) != 0:
            v = int(input("Mida soovite muuta, parooli(0) või nime(1)?"))
            if v == 0:
                while True:
                    v = input("Kas soovite parooli geniseerida või ise välja mõelda? ")
                    if v.upper() == "JAH":
                        new_user, y = Registration(nimi)
                        secret_word = input("Mõtle välja salajane sõna! ")
                        new_user["secret_word"] = secret_word
                        user.append(new_user)
                        user_data.append(new_user)
                        max_id = y
                        break
                    elif v.upper() == "EI":
                        password = input("Mõtle välja parool ")
                        perm, answer = PasswordCheck(password)
                        if not perm:
                            print(answer)
                        else:
                            break
                    else:
                        print("Kirjutage palun JAH või EI")
                user_data["user_password"] = password
            elif v == 1:
                new_name = input("New name ")
                user_data["user_name"] = new_name
            else:
                pass
    if v == 3:
        pass
    if v == 404:
        break
    else:
        pass
