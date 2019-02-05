import datetime
import random
import re


def kiedystolat():
    '''
Ćwiczenie 1
Stwórz program, który prosi użytkownika o podanie jego imienia i nazwiska
oraz wieku. Wydrukuj skierowaną do nich wiadomość, która powie im rok,
w którym ukończą 100 lat.
'''

    imie = input("Podaj imię: ")
    nazwisko = input("Podaj nazwisko: ")

    teraz = str(datetime.datetime.now())
    rok_biezacy = int(teraz[0:4])

    wiek = int(input("Ile masz lat: "))
    rok_urodzenia = rok_biezacy - wiek
    rok_sto_lat = rok_urodzenia + 100
    za_ile_lat = 100 - wiek

    print(imie, nazwisko, "!!! W roku ", rok_sto_lat, "czyli za", za_ile_lat, "lat/a będziesz miał 100 lat!!!")


def suma_cyfr():
    '''
    (str) -> int

    Funkcja zwraca sumę cyfr podanej liczby.
    
    >>> suma_cyfr(125)
    8
    >>> suma_cyfr(10203040999)
    34

    '''

    liczbatekst = input("Podaj liczbę: ")
    liczba = 0
    for cyfra in liczbatekst:
        liczba = liczba + int(cyfra)

    return liczba

    '''    
    liczba = (int(liczbatekst))
    liczba1 = int(liczbatekst[0])
    liczba2 = int(liczbatekst[1])
    liczba3 = int(liczbatekst[2])
    suma = liczba1 + liczba2 + liczba3
    return suma
        '''


def fibonacci():
    '''
    (int) -> int

    Funkcja zwraca liczbę n pierwszych liczb ciągu fibonacciego. Użytkownik podaje liczbę n.

    >>> fibonacci(3)
        1
        1
        2
    >>> fibonacci(10)
        1
        1
        2
        3
        5
        8
        13
        21
        34
        55
    '''

    ile_liczb = int(input("Podaj ile pierwszych liczb ciągu Fibonacciego wygenerować: "))

    i = 1
    liczba1 = 1
    liczba2 = 1
    liczba = liczba1 + liczba2

    if ile_liczb == 0:
        return ("smutek, zero liczb")

    elif ile_liczb == 1:
        print(liczba1)

    elif ile_liczb == 2:
        print(liczba1)
        print(liczba2)

    elif ile_liczb > 2:
        print(liczba1)
        print(liczba2)
        ciag = [1, 1]
        while i < (ile_liczb - 1):
            ciag.append(ciag[i] + ciag[i - 1])
            i = i + 1
            print(ciag[i])


def fibonacci_lista():
    num = int(input("How many numbers that generates?:"))
    i = 1
    if num == 0:
        fib = []
    elif num == 1:
        fib = [1]
    elif num == 2:
        fib = [1, 1]
    elif num > 2:
        fib = [1, 1]
        while i < (num - 1):
            fib.append(fib[i] + fib[i - 1])
            i += 1
    return fib
    print(fibonacci_lista())


def ktory_znak(tekst, litera):
    '''
    (str,str) -> int
    Funkcja zwraca pierwszy numer znaku odnalezionego w tekscie
    >>> ktory_znak('ala ma kota','k')
    7
    >>> ktory_znak('kot ma ale','o')
    1
    '''

    wynik = tekst.index(litera)
    return wynik


def male_litery(tekst):
    male = str.lower(tekst)
    return male


def element_search():
    list = input("podaj dowolną listę liczb: ")
    number = input("szukana liczba: ")

    if number in list:
        return True
    else:
        return False


def wszystkie_dzielniki():
    # funkcja zwraca wszystkie dzielniki podanej liczby

    liczba = int(input("podaj liczbę: "))

    num = 1
    lista_dzielnikow = []

    while num <= liczba:
        if liczba % num == 0:
            lista_dzielnikow.append(num)
        num = num + 1

    return lista_dzielnikow


def elementy_listy_mniejsze_niz():
    # dla podanej listy 20 elementow, zwracana jest druga lista elementów mniejszych niż 50
    lista = []
    lista_mniejsze_niz = []
    num = 0

    while num < 20:
        x = random.randint(1, 100)
        lista.append(x)

        if lista[num] < 50:
            lista_mniejsze_niz.append(lista[num])

        num = num + 1

    print(lista)
    print(lista_mniejsze_niz)


def elementy_wspolne_dwoch_list():
    '''
    Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements
that are common between the lists (without duplicates). Make sure your
program works on two lists of different sizes.

    >>> elementy_wspolne_dwoch_list()
    [1, 2, 8, 13]

    '''

    i = 0

    a = []
    b = []

    while i < 10:
        x = random.randint(1, 15)
        y = random.randint(1, 15)
        a.append(x)
        b.append(y)
        i = i + 1
    print("[a] =", a)
    print("[b] =", b)

    # ab - lista zawierajaca elementy wspolne list a i b
    ab = []
    num = 0

    while num < len(a):
        if a[num] in b:
            ab.append(a[num])
        num = num + 1
    '''
    Funkcja set tworzy kolekcję uporządkowanych i unikalnych elementów. Natomiast funkcja list zamienia kolekcję w listę. 
    >>> list = [1,1,1,2]
    >>> set(list)
    {1, 2}
    '''
    new_list = list(set(ab))
    new_list.sort()
    print("[ab] =", new_list)


def palindrom():
    tekst = input("Podaj słowo: ")
    tekst = str.lower(tekst)
    tekst = re.sub("[^a-zA-Z]", "", tekst)

    i = 0
    while i < len(tekst):
        if tekst[i] == tekst[-1 - i]:
            print(tekst[i], tekst[-1 - i])
            i = i + 1
            wynik = 0

        else:
            wynik = 1
            break

    if wynik == 0:
        print("To jest palindrom")
    else:
        print("To nie jest palindrom")


''' z użyciem for:
    for i in range(len(tekst)):
        if(tekst[i] == tekst[-i-1]):
            wynik=0
        else:
            wynik=1
            break

'''


def papier_kamien_nozyce():
    seq = ['p', 'k', 'n']

    g1 = random.choice(seq)
    g2 = random.choice(seq)

    print(g1, g2)

    tab = [['p', 'p', 're'], ['p', 'k', 'g1'], ['p', 'n', 'g2'], ['k', 'k', 're'], ['k', 'p', 'g2'], ['k', 'n', 'g1'],
           ['n', 'n', 're'], ['n', 'p', 'g1'], ['n', 'k', 'g2']]

    i = 0
    while i <= 8:
        if tab[i][0] == g1 and tab[i][1] == g2:
            wynik = tab[i][2]
            print(wynik)
        i = i + 1

    return wynik


def pkn_ile_gier():
    ile = int(input("Ile gier: "))
    tab = []

    num = 0
    while num < ile:
        tab.append(papier_kamien_nozyce())
        num = num + 1
    print(tab)

    g1_w = tab.count('g1')
    g2_w = tab.count('g2')
    re_w = tab.count('re')

    print("wygranych g1: ", g1_w)
    print("wygranych g2: ", g2_w)
    print("remisów: ", re_w)

    kto_wygral = max(g1_w, g2_w, re_w)

    return kto_wygral


'''
>>>>>>>>>>>>>>>> ODP Z ZADANIA
import sys

user1 = input("What's your name?")
user2 = input("And your name?")
user1_answer = input("%s, do yo want to choose rock, paper or scissors?" % user1)
user2_answer = input("%s, do you want to choose rock, paper or scissors?" % user2)

def compare(u1, u2):
    if u1 == u2:
        return("It's a tie!")
    elif u1 == 'rock':
        if u2 == 'scissors':
            return("Rock wins!")
        else:
            return("Paper wins!")
    elif u1 == 'scissors':
        if u2 == 'paper':
            return("Scissors win!")
        else:
            return("Rock wins!")
    elif u1 == 'paper':
        if u2 == 'rock':
            return("Paper wins!")
        else:
            return("Scissors win!")
    else:
        return("Invalid input! You have not entered rock, paper or scissors, try again.")
        sys.exit()

print(compare(user1_answer, user2_answer))
'''


def zgadnij_liczbe():
    user = input("Podaj imię: ")
    max = int(input("%s, podaj max liczbę, do której zgadujemy: " % user))

    szukana = random.randint(1, max)

    i = 0
    while i < max:

        user_typ = int(input("szukana liczba to: "))

        if user_typ == szukana:
            print("Brawo! Zgadłeś!")
            break
        elif user_typ < szukana:
            print("Szukana liczba jest większa")
        else:
            print("Szukana liczba jest mniejsza")

        i = i + 1

    return szukana


def tab_mnoz():
    # tabliczka mnozenia 10x10
    i = 1
    j = 1
    tab = []

    for j in range(1, 11, 1):
        for i in range(1, 11, 1):
            wynik = j * i
            # kolumny równe na 3 znaki + zamiana na stringi
            tab.append("%3i" % wynik)

        i = 1
    # print(tab)

    # wydruk w listach po 10 elementów
    k = 1
    for k in range(1, 11, 1):
        t = k * 10
        print(tab[t - 10:t])


"""
>>> tab_mnoz()
['  1', '  2', '  3', '  4', '  5', '  6', '  7', '  8', '  9', ' 10']
['  2', '  4', '  6', '  8', ' 10', ' 12', ' 14', ' 16', ' 18', ' 20']
['  3', '  6', '  9', ' 12', ' 15', ' 18', ' 21', ' 24', ' 27', ' 30']
['  4', '  8', ' 12', ' 16', ' 20', ' 24', ' 28', ' 32', ' 36', ' 40']
['  5', ' 10', ' 15', ' 20', ' 25', ' 30', ' 35', ' 40', ' 45', ' 50']
['  6', ' 12', ' 18', ' 24', ' 30', ' 36', ' 42', ' 48', ' 54', ' 60']
['  7', ' 14', ' 21', ' 28', ' 35', ' 42', ' 49', ' 56', ' 63', ' 70']
['  8', ' 16', ' 24', ' 32', ' 40', ' 48', ' 56', ' 64', ' 72', ' 80']
['  9', ' 18', ' 27', ' 36', ' 45', ' 54', ' 63', ' 72', ' 81', ' 90']
[' 10', ' 20', ' 30', ' 40', ' 50', ' 60', ' 70', ' 80', ' 90', '100']
>>> 
"""


def tab_mnoz_rownania():
    for x in range(1, 11):
        for y in range(1, 11):
            # print(x,'**', y, '=' , x*y , '...')
            print('{}\t'.format(x * y), end='')


# tutaj tylko zwinięcie, po rozciągnieciu ekranu wiecej niz 10!!


def tab_mnoz_rown_tylko_wyniki():
    for x in range(1, 11):
        print('\t')
        for y in range(1, 11):
            print("%4i" % (x * y), end='')


"""
>>> tab_mnoz_rown_tylko_wyniki()
	
   1   2   3   4   5   6   7   8   9  10	
   2   4   6   8  10  12  14  16  18  20	
   3   6   9  12  15  18  21  24  27  30	
   4   8  12  16  20  24  28  32  36  40	
   5  10  15  20  25  30  35  40  45  50	
   6  12  18  24  30  36  42  48  54  60	
   7  14  21  28  35  42  49  56  63  70	
   8  16  24  32  40  48  56  64  72  80	
   9  18  27  36  45  54  63  72  81  90	
  10  20  30  40  50  60  70  80  90 100
>>> 
"""


def tab_mnoz3():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print('{}x{}={}\t'.format(i, j, i * j), end='')
        print()


"""
1x1=1	
2x1=2	2x2=4	
3x1=3	3x2=6	3x3=9	
4x1=4	4x2=8	4x3=12	4x4=16	
5x1=5	5x2=10	5x3=15	5x4=20	5x5=25	
6x1=6	6x2=12	6x3=18	6x4=24	6x5=30	6x6=36	
7x1=7	7x2=14	7x3=21	7x4=28	7x5=35	7x6=42	7x7=49	
8x1=8	8x2=16	8x3=24	8x4=32	8x5=40	8x6=48	8x7=56	8x8=64	
9x1=9	9x2=18	9x3=27	9x4=36	9x5=45	9x6=54	9x7=63	9x8=72	9x9=81	
"""


def wyrownanie_do_prawej():
    for x in range(5, 100, 10):
        print("%4i%6i%8i" % (x, x ** 2, x ** 3))


"""

Funkcja ustala dlugosc pola na kolejno 4,6,8 znakow
   5    25     125
  15   225    3375
  25   625   15625
  35  1225   42875
  45  2025   91125
  55  3025  166375
  65  4225  274625
  75  5625  421875
  85  7225  614125
  95  9025  857375
"""


def cows_and_bulls():
    szukana = str(random.randint(1000, 9999))
    print('szukana: ', szukana)

    print('Witaj w grze Cows and Bulls!!\n')
    num = 0
    user_try = 0

    while num != szukana:

        try:
            num = input('Podaj liczbę: ')
        except:
            print('nieprawidłowy format, spróbuj jeszcze raz')

        bulls_count = 0
        cows_count = 0
        tab_sys = []
        tab_user = []
        for i in range(0, len(szukana)):
            tab_sys.append(szukana[i])
        # print(tab_sys)

        for j in range(0, len(num)):
            tab_user.append(num[j])
        # print(tab_user)

        for k in range(0, 4):
            if tab_sys[k] == tab_user[k]:
                cows_count = cows_count + 1
            elif tab_user[k] in tab_sys:
                bulls_count = bulls_count + 1

        if cows_count == 1:
            cows_text = 'cow, '
        else:
            cows_text = 'cows, '

        if bulls_count == 1:
            bulls_text = 'bull'
        else:
            bulls_text = 'bulls'

        print(cows_count, cows_text, bulls_count, bulls_text)
        user_try += 1
    print(f'Tak, to jest szukana liczba!!! Zgadłeś w {user_try} próbie.')


"""
Create a program that will play the “cows and bulls” game with the user. The game works like this:
Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the user guessed correctly in the correct place, they have a “cow”. For every digit the user guessed correctly in the wrong place is a “bull.” Every time the user makes a guess, tell them how many “cows” and “bulls” they have. Once the user guesses the correct number, the game is over. Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.
Say the number generated by the computer is 1038. An example interaction could look like this:

Welcome to the Cows and Bulls Game! 
Enter a number: 
>>> 1234
2 cows, 0 bulls
>>> 1256
1 cow, 1 bull
...
"""


def both_start_with(s1, s2, prefix):
    '''(str, str, str) -> bool

    Return True if and only if s1 and s2 both start with the       letters in prefix.
    '''
    #    if s1.startswith(prefix) and s2.startswith(prefix):
    #        return True
    #    else:
    #        return False

    return s1.startswith(prefix) and s2.startswith(prefix)


def double_values(collection):
    for v in range(len(collection)):
        collection[v] = collection[v] * 2
    return collection


'''
>>> double_values([1,2,3])
[2, 4, 6]

>>> double_values({0:10, 1:20, 2:30})
{0: 20, 1: 40, 2: 60}

DLA TYCH PRZYPADKÓW NIE ZADZIAŁA:

>>> double_values('123')
	
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    double_values('123')
  File "C:\DATA SCIENCE KURS\cwiczenia_z_internetow.py", line 559, in double_values
    collection[v] = collection[v] * 2
TypeError: 'str' object does not support item assignment
>>> double_values((1,2,3))
	
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    double_values((1,2,3))
  File "C:\DATA SCIENCE KURS\cwiczenia_z_internetow.py", line 559, in double_values
    collection[v] = collection[v] * 2
TypeError: 'tuple' object does not support item assignment
>>> double_values({1:10, 2:20, 3:30})
	
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    double_values({1:10, 2:20, 3:30})
  File "C:\DATA SCIENCE KURS\cwiczenia_z_internetow.py", line 559, in double_values
    collection[v] = collection[v] * 2
KeyError: 0
'''


# zad. 8 final test
def gather_every_nth(L, n):
    result = []
    i = 0
    while i < len(L):
        result.append(L[i])
        i = i + n  # było do uzupełnienia

    return result


'''(list, int) -> list

    Return a new list containing every n'th element in L, starting at index 0.

    Precondition: n >= 1

    >>> gather_every_nth([0, 1, 2, 3, 4, 5], 3)

    [0, 3]
    >>> gather_every_nth(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'], 2)
   ['a', 'c', 'e', 'g', 'i']
'''


# zad.9 final test
def get_keys(L, d):
    '''(list, dict) -> list

    Return a new list containing all the items in L that are keys in d.

    >>> get_keys([1, 2, 'a'], {'a': 3, 1: 2, 4: 'w'})
    [1, 'a']
    '''

    result = []
    for k in L:  # było do uzupełnienia
        if k in d:
            result.append(k)

    return result


# zad.10 final test
def are_lengths_of_strs(L1, L2):
    '''(list of int, list of str) -> bool
  
    Return True if and only if all the ints in L1 are the lengths of the strings
    in L2 at the corresponding positions.

    Precondition: len(L1) == len(L2)

    >>> are_lengths_of_strs([4, 0, 2], ['abcd', '', 'ef'])
    True
    >>> are_lengths_of_strs([4, 0, 2], ['abcde', '', 'ef'])
    False

    '''
    result = True
    for i in range(len(L1)):
        if L1[i] != len(L2[i]):
            result = False

    return result


# zad. 12 final test
def get_diagonal_and_non_diagonal(L):
    '''(list of list of int) -> tuple of (list of int, list of int)

    Return a tuple where the first item is a list of the values on the
    diagonal of square nested list L and the second item is a list of the rest
    of the values in L.

    >>> get_diagonal_and_non_diagonal([[1,  3,  5], [2,  4,  5], [4,  0,  8]])
    ([1, 4, 8], [3, 5, 2, 5, 4, 0])
    '''

    diagonal = []
    non_diagonal = []
    for row in range(len(L)):
        for col in range(len(L)):

            if row == col:
                diagonal.append(L[row][col])
            elif row != col:
                non_diagonal.append(L[row][col])

    return (diagonal, non_diagonal)


# zad. 13 final test
def add_to_letter_counts(d, s):
    '''(dict of {str: int}, str) -> NoneType

    d is a dictionary where the keys are single-letter strings and the values
    are counts.

    For each letter in s, add to that letter's count in d.

    Precondition: all the letters in s are keys in d.

    >>> letter_counts = {'i': 0, 'r': 5, 'e': 1}
    >>> add_to_letter_counts(letter_counts, 'eerie')
    >>> letter_counts
    {'i': 1, 'r': 6, 'e': 4}
    '''

    for c in s:
        letter_counts[c] = letter_counts[c] + 1
    return letter_counts


# zad. 10 final test v2
def count_values_that_are_keys(d):
    '''(dict) -> int

    Return the number of values in d that are also keys in d.
   
    >>> count_values_that_are_keys({1: 2, 2: 3, 3: 3})
    3
    >>> count_values_that_are_keys({1: 1})
    1
    >>> count_values_that_are_keys({1: 2, 2: 3, 3: 0})
    2
    >>> count_values_that_are_keys({1: 2})
    0
    '''

    result = 0
    for k in d:
        if d[k] in d:  # bylo do uzupelnienia
            result = result + 1

    return result


# zad.12 v2 final test
def get_negative_nonnegative_lists(L):
    '''(list of list of int) -> tuple of (list of int, list of int)

    Return a tuple where the first item is a list of the negative ints in the
    inner lists of L and the second item is a list of the non-negative ints
    in those inner lists.

    Precondition: the number of rows in L is the same as the number of
    columns.

    >>> get_negative_nonnegative_lists([[-1,  3,  5], [2,  -4,  5], [4,  0,  8]])
    ([-1, -4], [3, 5, 2, 5, 4, 0, 8])
    '''

    nonneg = []
    neg = []
    for row in range(len(L)):
        for col in range(len(L)):
            if L[row][col] < 0:
                neg.append(L[row][col])
            else:
                nonneg.append(L[row][col])

    return (neg, nonneg)
