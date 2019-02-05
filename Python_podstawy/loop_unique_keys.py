'''

    Mając bazę danych z listingu poniżej
    Wygeneruj listę unikalnych kluczy dictów

DATABASE = [
    {'last_name': 'Jiménez'},
    {'first_name': 'Mark', 'last_name': 'Watney'},
    {'first_name': 'Иван', 'age': 42},
    {'first_name': 'Matt', 'last_name': 'Kowalski', 'born': 1961},
    {'first_name': 'José', 'born': 1961, 'agency': 'NASA'},
]

Algorithm:

    Iteruj po rekordach w bazie danych
    Z rekordu wyciągnij klucze
    Dodaj klucze do zbioru
    Usuń duplikaty w zbiorze

'''

DATABASE = [
    {'last_name': 'Jiménez'},
    {'first_name': 'Mark', 'last_name': 'Watney'},
    {'first_name': 'Иван', 'age': 42},
    {'first_name': 'Matt', 'last_name': 'Kowalski', 'born': 1961},
    {'first_name': 'José', 'born': 1961, 'agency': 'NASA'},
    ]

my_set = set()

for element in DATABASE:
    for key in element:
        my_set.add(key)

print(my_set)