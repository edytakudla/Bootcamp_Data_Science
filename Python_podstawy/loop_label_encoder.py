'''

    Mając do dyspozycji zbiór danych Irysów z Code Listing 11.1.
    Ze zbioru wyodrębnij dane odrzucając nagłówek.
    Przemieszaj elementy zbioru danych
    Stwórz słownik gatunków species, gdzie kolejnym liczbom naturalnym zaczynając od zera przyporządkuj gatunek irysów.
    Klucze muszą być wygenerowane na podstawie kolejności występowania gatunków w przemieszanym zbiorze danych:

        species = {
            0: 'versicolor',
            1: 'virginica',
            2: 'setosa'
        }

    Przygotuj listę cech (labels) z kluczami ze słownika gatunków.
    Etykiety muszą być wygenerowane na podstawie kolejności w przemieszanym zbiorze danych:

        print(labels)
        # [0, 1, 2, 1, 1, 0, ...]

    Wyświetl na ekranie species oraz labels

Algorithm:

    Wyodrębnij dane odrzucając nagłówek
    Przemieszaj elementy zbioru danych
    Stwórz słownik gatunków species
    Iteruj po elementach zbioru danych
    Gatunek to ostatni element rekordu
    Jeżeli w słowniku nie ma gatunku, to dodaj go z kolejnym numerem
    Do listy label dodawaj wartość słownika gatunków dla gatunku w tym rekordzie
    Odwróć słownik gatunków
    Wyświetl na ekranie species oraz labels

'''


#SKONCZYC!!!!!!! wynik ma byc postaci {0: 'setosa', 1: 'versicolor', 2: 'virginica'}

import random
DATA = [
    ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
    (5.1, 3.5, 1.4, 0.2, 'setosa'),
    (4.9, 3.0, 1.4, 0.2, 'setosa'),
    (4.7, 3.2, 1.3, 0.2, 'setosa'),
    (4.6, 3.1, 1.5, 0.2, 'setosa'),
    (5.0, 3.6, 1.4, 0.3, 'setosa'),
    (5.4, 3.9, 1.7, 0.4, 'setosa'),
    (4.6, 3.4, 1.4, 0.3, 'setosa'),
    (7.0, 3.2, 4.7, 1.4, 'versicolor'),
    (6.4, 3.2, 4.5, 1.5, 'versicolor'),
    (6.9, 3.1, 4.9, 1.5, 'versicolor'),
    (5.5, 2.3, 4.0, 1.3, 'versicolor'),
    (6.5, 2.8, 4.6, 1.5, 'versicolor'),
    (5.7, 2.8, 4.5, 1.3, 'versicolor'),
    (5.7, 2.8, 4.1, 1.3, 'versicolor'),
    (6.3, 3.3, 6.0, 2.5, 'virginica'),
    (5.8, 2.7, 5.1, 1.9, 'virginica'),
    (7.1, 3.0, 5.9, 2.1, 'virginica'),
    (6.3, 2.9, 5.6, 1.8, 'virginica'),
    (6.5, 3.0, 5.8, 2.2, 'virginica'),
    (7.6, 3.0, 6.6, 2.1, 'virginica'),
    (4.9, 2.5, 4.5, 1.7, 'virginica'),
]

header = DATA[0]
data = DATA[1:]
random.shuffle(data)

# słownik gatunków species
my_set = set()

for tupla in data:
    print(tupla[4])
    my_set.add(tupla[4])
print(my_set)
l = list(my_set)

dict = {}
i = 0
for element in my_set:
    dict[i] = l[i]
    i = i+1
print(f'species: {dict}')





'''
data - DATA[1:]
species = dict()
labels = list()
features = list()

for record in data:
    species_in_record = record[4]
    features.append(record[:4]

    if species_in_record not in species.keys():
        species[species_in_record] = len(species)
    labels.append(species[species_in_record]) # odwrócone wartosci set : 0, vir: 1...

# odwrócenie dicta
species = {v: k for k, v in species.items()}

# to samo inaczej:
# for k, v in species in spacies.items()

print(species)
print(labels)
print(features)



unique_keys = set()
for row in DATA:
    unique_keys.update(row.keys())
print('******', unique_keys)
'''
