'''

    Wczytaj od użytkownika imię
    Za pomocą f-string formatting wyświetl na ekranie:
'''
#        '''My name... "José Jiménez".
#                I'm an """astronaut!"""'''
'''
    Uwaga! Druga linijka zaczyna się od tabulacji
    Gdzie wartość w podwójnym cudzysłowiu to ciąg od użytkownika (w przykładzie użytkownik wpisał José Jiménez)
    Zwróć uwagę na znaki apostrofów, cudzysłowów, tabulacji i nowych linii
    W ciągu do wyświetlenia nie używaj spacji ani enterów - użyj \n i \t
    Tekst wyświetlony na ekranie ma mieć zamienione wszystkie spacje na _
    Tekst wyświetlony na ekranie ma być w UPPERCASE
    Nie korzystaj z dodawania stringów (str + str)
    Następnie znów wyświetl na ekranie wynik, tym razem z podmienionymi spacjami:
'''
#        '''MY_NAME_"JOSÉ_JIMÉNEZ".
#        _I'M_AN_"""ASTRONAUT!"""'''




name = input('What is your name: ')
# uzycie f"""....."""
s2 = f"""'''My name... "{name}".\n\t\tI'm an \"\"\"astronaut!\"\"\"'''"""
print(s2)

t = s2.replace(' ','_')
print(t)

z = t.upper()
print(z)
