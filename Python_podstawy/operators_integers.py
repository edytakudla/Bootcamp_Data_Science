'''

    Wczytaj liczbę od użytkownika (poda tylko int albo float)
    Wyświetl informację czy jest to liczba całkowita, czy niecałkowita.

'''

number_float = float(input('Podaj liczbe: '))
number_int = float(int(number_float))
rest = number_float - number_int
if rest == 0.0:
    print('całkowita')
else:
    print('niecałkowita')