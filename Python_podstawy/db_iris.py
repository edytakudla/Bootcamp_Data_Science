"""
1.12.1. Iris Database

    Pobierz dane z listingu Code Listing 1.29.
    Bazę pomiarów Irysów przekonwertuj na tabelę w sqlite3
    Nazwy poszczególnych kolumn:

            id - int
            species - str
            datetime - datetime
            sepal_length - float
            sepal_width - float
            petal_length - float
            petal_width - float

    Do połączenia wykorzystaj context manager (with)
    Dane wrzuć do bazy za pomocą .executemany() podając dict
    Do bazy danych zapisz species jako nazwę gatunku (str), a nie jego id (int) (wersja z gwiazdką: nie korzystaj z if-ów do tego)
    Dodaj kolumnę datetime z datą i czasem dodania (UTC)
    Załóż index na datetime
    Wyniki wypisz z bazy danych (SELECT * FROM iris ORDER BY datetime DESC)
    Zwracaj dane jako sqlite3.Row

Code Listing 1.29. Iris Database¶

dane w kolejnosci:

sepal_length, sepal_width, petal_length, petal_width, species
4.3,3.0,1.1,0.1,0
5.8,4.0,1.2,0.2,0
5.7,4.4,1.5,0.4,1
5.4,3.9,1.3,0.4,2
5.1,3.5,1.4,0.3,1
5.7,3.8,1.7,0.3,0
5.1,3.8,1.5,0.3,0
5.4,3.4,1.7,0.2,1
5.1,3.7,1.5,0.4,0
4.6,3.6,1.0,0.2,0
5.1,3.3,1.7,0.5,2
4.8,3.4,1.9,0.2,0
5.0,3.0,1.6,0.2,1
5.0,3.4,1.6,0.4,2
5.2,3.5,1.5,0.2,1
5.2,3.4,1.4,0.2,2
4.7,3.2,1.6,0.2,0

slownik dla species:
        0 - setosa
        1 - versicolor
        2 - virginica
"""

from datetime import datetime, timezone
import sqlite3

DANE = """4.3,3.0,1.1,0.1,0
5.8,4.0,1.2,0.2,0
5.7,4.4,1.5,0.4,1
5.4,3.9,1.3,0.4,2
5.1,3.5,1.4,0.3,1
5.7,3.8,1.7,0.3,0
5.1,3.8,1.5,0.3,0
5.4,3.4,1.7,0.2,1
5.1,3.7,1.5,0.4,0
4.6,3.6,1.0,0.2,0
5.1,3.3,1.7,0.5,2
4.8,3.4,1.9,0.2,0
5.0,3.0,1.6,0.2,1
5.0,3.4,1.6,0.4,2
5.2,3.5,1.5,0.2,1
5.2,3.4,1.4,0.2,2
4.7,3.2,1.6,0.2,0
"""    # dzielimy nasza liste na linie po  -> wtedy dodac .split('\n')

print(DANE)
# ['4.3,3.0,1.1,0.1,0', '5.8,4.0,1.2,0.2,0', '5.7,4.4,1.5,0.4,1', '5.4,3.9,1.3,0.4,2', '5.1,3.5,1.4,0.3,1', '5.7,3.8,1.7,0.3,0', '5.1,3.8,1.5,0.3,0', '5.4,3.4,1.7,0.2,1', '5.1,3.7,1.5,0.4,0', '4.6,3.6,1.0,0.2,0', '5.1,3.3,1.7,0.5,2', '4.8,3.4,1.9,0.2,0', '5.0,3.0,1.6,0.2,1', '5.0,3.4,1.6,0.4,2', '5.2,3.5,1.5,0.2,1', '5.2,3.4,1.4,0.2,2', '4.7,3.2,1.6,0.2,0', '']


SQL_CREATE_TABLE = """
    CREATE TABLE IF NOT EXISTS iris (
        id INTEGER PRIMARY KEY AUTOINCREMENT,       
        species TEXT,
        datetime DATETIME,                  
        sepal_length REAL,                  
        sepal_width REAL,
        petal_length REAL,
        petal_width REAL
        
    )

"""
# autoincrement bedzie podbijal licznik o 1
# tak naprawde ilosc sekund jakie uplynely od 0.01.1970
# w pythonie FLOAT odpowiada REAL w SQL

SQL_CREATE_INDEX = """
    CREATE INDEX IF NOT EXISTS
    iris_datetime_index ON iris (datetime)
"""

SQL_INSERT = """
    INSERT INTO iris (
        species, 
        datetime,
        sepal_length,
        sepal_width,
        petal_length,
        petal_width)
    VALUES (
        :species, 
        :datetime,
        :sepal_length,
        :sepal_width,
        :petal_length,
        :petal_width
    )

"""

SQL_SELECT = 'SELECT * FROM iris ORDER BY datetime DESC'

lista_rekordow = []

for rekord in DANE.split():
    print(rekord)
    pomiary = rekord.split(',')
    sepal_length = float(pomiary[0])
    sepal_width = float(pomiary[1])
    petal_length = float(pomiary[2])
    petal_width = float(pomiary[3])
    species = int(pomiary[4])


    if species == 0:
        species = 'setosa'
    elif species == 1:
        species = 'versicolor'
    else:
        species = 'virginica'

    print(species)

    datetime = datetime.now(tz=timezone.utc)

    lista_rekordow.append({

        'datetime': datetime,
        'species': species,
        'sepal_length': sepal_length,
        'sepal_width': sepal_width,
        'petal_length': petal_length,
        'petal_width': petal_width,


    })


# utworzenie bazy danych z kolumnami podanymi w sql_create_table, iris.sqlite3 to plik
with sqlite3.connect('iris.sqlite3') as db:
    db.execute(SQL_CREATE_TABLE)
    db.execute(SQL_CREATE_INDEX)
    db.executemany(SQL_INSERT, lista_rekordow)

for row in db.execute(SQL_SELECT):
  #  row = dict(row)
    print(row)

# sepal_len = line.split(',')[0]
# sepal_wid = line.split(',')[1]
# petal_len = line.split(',')[2]
# petal_wid = line.split(',')[3]
"""
zamiast ifow mozna uzyc slownika

    species_dict = {'0' : 'setosa',
                    '1' : 'versicolor',
                    '2' : 'virginica',}

    species = species_dict.get(int(pomiary[4])  #jesli dojdzie kolejny gatunek ktorego nie ma w slowniku to zwroci None
    species = species_dict.get(int(pomiary[4])  #jesli dojdzie kolejny gatunek ktorego nie ma w slowniku to rzuci exception
"""
