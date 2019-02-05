'''

    napisz program, który wczyta od użytkownika ciąg znaków
    sprawdzi czy jest to liczba parzysta, czy nieparzysta.
    ZERO JEST PARZYSTE!!!!

'''

number = int(float(input('Podaj liczbę: ')))
if number % 2 == 0:
    print('parzysta')
else:
    print('nieparzysta')
