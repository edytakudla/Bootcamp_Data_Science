'''

    Napisz program, który poprosi użytkownika o wiek
    Użytkownik będzie podawał tylko i wyłącznie int lub float
    Następnie sprawdzi pełnoletność i wyświetli informację czy osoba jest “dorosła” czy “niepełnoletnia”
'''

wiek = float(input('Podaj ile masz lat: '))
ADULT = 18.0

if wiek >= ADULT:
    print('dorosła')
else:
    print('niepełnoletnia')