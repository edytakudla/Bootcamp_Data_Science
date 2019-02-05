'''

    Stwórz tuple z cyframi od 0-9
    Przekonwertuj ją do list
    Na pierwsze miejsce w liście dodaj całą oryginalną tuple
    Przekonwertuj wszystko na płaski set unikalnych wartości wykorzystując slice

    >>> n = [5,6,7]
    [5, 6, 7]
    >>> n.insert(20,2)
    [5, 6, 7, 2]
    >>> n.insert(2,20)
    [5, 6, 20, 7, 2]
    >>> n.insert(1,[50,60])
    [5, [50, 60], 6, 20, 7, 2]
    >>> n.extend('ABC')
    [5, [50, 60], 6, 20, 7, 2, 'A', 'B', 'C']
    >>> n.extend('555') nie można dodawac inta 555 !!
    [5, [50, 60], 6, 20, 7, 2, 'A', 'B', 'C', '5', '5', '5']
    >>> n.extend([80,90])
    [5, [50, 60], 6, 20, 7, 2, 'A', 'B', 'C', '5', '5', '5', 80, 90]
    >>> n.extend([[80,90]])
    [5, [50, 60], 6, 20, 7, 2, 'A', 'B', 'C', '5', '5', '5', 80, 90, [80, 90]]

    ROZNICA MIEDZY SET A DICT!
    >>> set = {1,2,3}
    {1, 2, 3}
    >>> dict = {'A':1, 'B':2, 'C':3}
    {'A': 1, 'B': 2, 'C': 3}

    >>> set = {1, 3, 3, 5}
    {1, 3, 5}
    >>> set.update([6, 9]) DODANIE LISTY DO SETA
    {1, 3, 5, 6, 9}
    >>> set.update((10,20)) DODANIE TUPLI DO SETA
    {1, 3, 5, 6, 9, 10, 20}


'''

print('PRZYKLAD 1\n')
tuple = (0,1,2,3,4,5,6,7,8,9)
# konwertuj do listy
new_list = list(tuple)
print(f'lista: {new_list}')
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# wstaw na miejsce nr 0 oryginalna tuple
new_list.insert(0, tuple)
print(f'lista z tupla: {new_list}')

# konwersja na set, tutaj tupla jako ostatnia wartosc SET NIE ZACHOWUJE KOLEJNOSCI, DLATEGO TUPLA PONOWNIE NA KONCU!!!
d = set(new_list[0])
print(f'pierwszy element z listy - zamiana tupli na set: {d}')

d.update(new_list[0:1])
print(f'set z tupla: {d}')


print('\nPRZYKLAD 2\n') # zrobic set {1, 2, 3, 4, 5, 6}
l = [1, 2, 3, (4, 5, 6)]
print(l)    # {4, 5, 6}
s = set(l[-1])
print(s)    # {1, 2, 3}
rest = set(l[0:-1])
print(rest)
rest.update(s) # {1, 2, 3, 4, 5, 6}
print(rest)



'''
# wstaw tuple na miejsce nr 0
c.insert(0, tuple)
print(c)
d = set(c[0])
d.update(c[:1])
print(d)


list = []
my_set = set()

for item in tuple:
    list.append(tuple[item])
print(list)

my_set.update(list)
print(my_set)
'''