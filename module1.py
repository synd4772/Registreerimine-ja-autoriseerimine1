import string
from random import *
y = string.octdigits
x = string.ascii_letters
z = string.punctuation
lst = [x, y, z]

user_data = [{
    "user_id": 1,
    "user_name": "Mark Piller",
    "user_password": "SA4K1NM#MFDA",
    "secret_word": "banana",
    "email":"mark.piller@gmail.com"
    },{
    "user_id": 2,
    "user_name": "John Doe",
    "user_password": "das34SsDczxma",
    "secret_word": "õun",
    "email":"john.doe@gmail.com"
    }]

max_id = 2

#def MakePassword(nimi):
#    while True:
#        v = input("Kas soovite parooli geniseerida või ise välja mõelda? ")
#        if v.upper() == "JAH":
#            new_user, y = Registration(nimi)
#            secret_word = input("Mõtle välja salajane sõna! ")
#            new_user["secret_word"] = secret_word
#            user.append(new_user)
#            user_data.append(new_user)
#            max_id = y
#            break
#        elif v.upper() == "EI":
#            password = input("Mõtle välja parool ")
#            perm, answer = PasswordCheck(password)
#            if not perm:
#                print(answer)
#            else:
#                break
#        else: 
#            print("Kirjutage palun JAH või EI")
#    return password

def KasutajaJareldus(user):
    pass

def CheckName(name):
    for i in name:
        pass
    pass

def PasswordGeneretion():
    password = ""
    for _ in range(0, randint(5,9)):
        x_ = randint(0,2)
        password += str(lst[x_][randint(0,len(lst[x_]) - 1)])
    return password

def PasswordCheck(password:str):
    if len(password) < 5:
        return False, "Paroolil peab olema vähemalt 5 tähemärki"
    for i in lst:
        for x in i:
            if list(password).count(x) == len(password):
                return False, "Parool ei tohi koosneda samadest sümbolitest"
        #if list(password).count(str([x for x in i])) == len(password):
        #    print("sümbol")
    string_ = ""
    for i in range(0,20):
        string_ += str(i)
        if password == string_ or password == string_[1:-1]:
            return False, "Keerulisemad salasõnad"
    return True, "success"

def FindUser(name):
    for i in user_data:
        if name == i.get("user_name"):
            return True, i
    return False, None

def Registration(name:str, password = PasswordGeneretion()):
    if FindUser(name) is False:
        return None, False
    x = {
    "user_id": max_id + 1,
    "user_name": name,
    "user_password": password
    }
    user_data.append(x)
    
    return x, max_id + 1

def Authorization(name, password):
    x, user = FindUser(name)
    if x is False:
        print(x, user)
        return False
    if password != user.get("user_password"):
        print(123)
        return False
     
    return user