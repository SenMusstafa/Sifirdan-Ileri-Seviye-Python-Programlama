class NameTooLongException(Exception):
    def __init__(self, message="Name alanı fazla karakter içeriyor"):
        self.message = message
        super().__init__(self.message)

class PasswordValidationException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def check_password(psw):
    import re
    if len(psw) < 8:
        raise PasswordValidationException("Parola en az 7 karakter olmalıdır")
    elif not re.search("[a-z]", psw):
        raise PasswordValidationException("Parola küçük harf içermelidir")
    elif not re.search("[A-Z]", psw):
        raise PasswordValidationException("Parola büyük harf içermelidir")
    elif not re.search("[0-9]", psw):
        raise PasswordValidationException("Parola rakam içermelidir")
    elif not re.search("[_@$]", psw):
        raise PasswordValidationException("Parola alfanümerik karakter içermelidir")
    elif re.search("\s", psw):
        raise PasswordValidationException("Parola boşluk içermemelidir")
    else:
        print("Geçerli parola")

class Person:
    def __init__(self, name, year):
        try:
            if len(name) > 10:
                raise NameTooLongException()
            else:
                self.name = name
        except NameTooLongException as ex:
            print(ex)

if __name__ == "__main__":
    x = 10
    if x > 5:
        raise Exception("x 5'ten büyük değer alamaz")

    password = "1234567aA_"
    try:
        check_password(password)
    except PasswordValidationException as ex:
        print(ex)
    else:
        print("Geçerli parola: else")
    finally:
        print("Validation tamamlandı")

    p = Person("Aliiiiiiiiiiiiii", 1989)
