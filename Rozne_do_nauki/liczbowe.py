import math

def potega_kwadrat(liczba):
    '''moj komentarz o tym, ze funkcja liczy kwadrat podanej liczby'''
    return liczba ** 2

def potega_wydruk(liczba):
    return print('wydruk: ', liczba**2)

def suma_policz(liczba1, liczba2):
    return liczba1+liczba2

def suma_drukuj(liczba1,liczba2):
    print(liczba1 + liczba2)
    
def drukuj_tabulator(a,b,c):
    print('a\tb\tc')

def spr_czy_parzysta(liczba):
    '''
(number) -> bool

Funkcja zwraca informacje czy podana liczba jest parzysta

>>> spr_czy_parzysta(4)
    True
>>> spr_czy_parzysta(7)
    False
'''
    reszta = liczba % 2
    return (reszta == 0)

def silnia(liczba):
    return math.factorial(liczba)

def sprawdzczypotega10(liczba):

    '''
(number) -> str

Funkcja sprawdza czy podana liczba jest potęgą liczby 10.

>>> sprawdzczypotega10(10)
'tak, podana liczba jest potęgą 10'
>>> sprawdzczypotega10(1000)
'tak, podana liczba jest potęgą 10'
>>> sprawdzczypotega10(2000)
'nie, podana liczba nie jest potęgą 10'
>>> sprawdzczypotega10(1001)
'nie, podana liczba nie jest potęgą 10'

'''


    tak = 'tak, podana liczba jest potęgą 10'
    nie = 'nie, podana liczba nie jest potęgą 10'
    
    if liczba != 0:
        modulo = liczba%10

        if modulo == 0:
            while liczba >= 10:
                liczba = liczba/10
            
                if liczba == 1.0:
                    wynik = tak
                else:
                    wynik = nie

        else:
            wynik = nie

    else:
        wynik = nie

    return (wynik)

