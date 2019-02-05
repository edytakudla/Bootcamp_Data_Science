login = ''

while login == '':
    login = input("Podaj login: ")
    if login == '':
        print('login nie może być pusty')

    else:
        password = '1'
        password2 = '2'

        while password != password2:

            password = input("Podaj hasło: ")
            password2 = input("Powtórz hasło: ")

            if password == password2:
                print("konto zostało utworzone")
            else:
                print("powtórzyłeś błędnie hasło")
