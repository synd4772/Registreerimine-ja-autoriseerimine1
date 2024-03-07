
from module1 import *
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
            while True:
                v = input("Kas soovite parooli geniseerida või ise välja mõelda? ")
                if v.upper() == "JAH":
                    new_user, y = Registration(nimi)
                    secret_word = input("Mõtle välja salajane sõna! ")
                    new_user["secret_word"] = secret_word
                    user.append(new_user)
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

            if len(user) == 0:
                new_user = Registration(nimi, password)
                secret_word = input("Mõtle välja salajane sõna! ")
                new_user["secret_word"] = secret_word
                user.append(new_user)
            print(user)
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
        pass
    if v == 3:
        pass
    if v == 404:
        break
