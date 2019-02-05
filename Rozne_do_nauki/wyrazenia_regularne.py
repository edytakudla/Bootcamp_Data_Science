import re

def kod_pin():
    tekst = """Wyobraz sobie, ze ten tekst zawiera numer
    PIN 9846 twojej karty 1122 do bankomatu, a ty wlasnie go
    zapomniales. Jak szybko go odnalezc?"""

    sciezka = r'\d\d\d\d'
    dopasowanie = re.search(sciezka, tekst)

    if dopasowanie: #Sprawdzamy czy udalo sie cos znalezc
        numer = dopasowanie.group()
        print(numer)


def wyr_reg1():

# Ponizej jest dokonywana lekka optymalizacja naszego wyrazenia
    pattern = re.compile(r"\[(on|off)\]")

# Teraz szukamy
    wynik = re.search(pattern, "Mono: Playback 65 [75%] [-16.50dB] [on]")
    print(wynik)
# Zwroci obiekt Match, jak chcemy wyświetlic, to dodatkowo group
    print(wynik.group())
    '''
    >>> wyr_reg1()
    <_sre.SRE_Match object; span=(35, 39), match='[on]'>
    [on]
    '''
    
    wynik2 = re.search(pattern, "Nada...:-(")
    print(wynik2)
    print(wynik2.group())
    '''
    wynik2 nic nie zwróci, wyrazenie niezgodne ze wzorcem. nie da sie grupować po None:
    None
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    wyr_reg1()
  File "C:/DATA SCIENCE KURS/wyrazenia_regularne.py", line 34, in wyr_reg1
    print(wynik2.group())
AttributeError: 'NoneType' object has no attribute 'group'
    '''

# Cwiczenie: skonstruj wyrazenie odpowiadajace adresowi email

def test_email(twoje_wyrazenie):
    wyrazenie = re.compile(twoje_wyrazenie)
    adresy = ["john@example.com", "python-list@python.org", '"wha.t.`1an?ug{}ly@email.com"']
    for adres in adresy:
        if not re.match(wyrazenie, adres):
            print("Nie udalo ci sie przyporzadkowac %s" % (adres))
        elif not twoje_wyrazenie:
            print("Nie wprowadziles wyrazenia do funkcji test_email")
        else:
            print("Dobrze")

wyrazenie = r'[a-z]@[a-z].[a-z]' # Tu wpisz swoje wyrazenie - ZLE!!!
test_email(wyrazenie)

def imie_wiek():

    name_age_table = []
    name_age_dictionary = {}

    NameAge = 'Ewa ma 25 a Janek 35 oraz Tomek 120'
    ages1 = re.findall(r'\d{1,1}', NameAge) # wszystkie cyfry pojedynczo
    # ['2', '5', '3', '5', '1', '2' ,'0']
    ages2 = re.findall(r'\d{1,2}', NameAge) # po dwie cyfry
    # ['25', '35', '12', '0']
    ages3 = re.findall(r'\d{1,3}', NameAge) # po trzy cyfry
    # ['25', '35', '120']

    names = re.findall(r'[A-Z][a-z]*',NameAge)

    print(ages3)
    print(names)

    # wydruk do tabeli
    i = 0
    for name in names:
        s = names[i]+': '+ages3[i]
        name_age_table.append(s)
        i = i+1
    print(name_age_table)
    # ['Ewa: 25', 'Janek: 35', 'Tomek: 120']

    #wydruk do słownika
    j = 0
    for name in names:
        #d[1]=2
        name_age_dictionary[names[j]]=ages3[j]
        j = j+1
    print(name_age_dictionary)
    # {'Ewa': '25', 'Janek': '35', 'Tomek': '120'}

def slowo_w_tekscie():

    s = 'Musi byc do wyboru. Zmieniac sie, zeby tylko nic sie nie zmienilo. To latwe, niemozliwe, trudne, warte proby.'

    # uzycie FINDALL, wyswietli liste slow, slowo prezentowane tyle razy ile razy wystepuje w tekscie

    szukaj_slowa = re.findall('zmienilo',s)
    szukaj_slowa2 = re.findall('niemozliwe, trudne',s)
    szukaj_slowa3 = re.findall('nie ma tej frazy',s)
    print(szukaj_slowa)
    print(szukaj_slowa2)
    print(szukaj_slowa3)

    # ['zmienilo']
    # ['niemozliwe, trudne']
    # []

    lista_slow_do_spr = ['zmienilo','niemozliwe, trudne', 'bla bla']

    i=0
    for slowo in lista_slow_do_spr:
        # uzycie SEARCH(slowo do sprawdzenia, caly tekst)
        if re.search(lista_slow_do_spr[i],s):
            print('Tak, slowo',lista_slow_do_spr[i],'wystepuje w tekscie')
        else:
            print('Nie, slowo',lista_slow_do_spr[i],'nie wystepuje w tekscie')
        i = i+1

    # Tak, slowo zmienilo wystepuje w tekscie
    # Tak, slowo niemozliwe, trudne wystepuje w tekscie
    # Nie, slowo bla bla nie wystepuje w tekscie

def slowo_w_tekscie_indexy():
    

    s = 'Musi byc do wyboru. Zmieniac sie, zeby tylko nic sie nie zmienilo. To latwe, niemozliwe, trudne, warte proby.'

    # uzycie FINDITER wskazuje na ktorym miejscu w tekscie zaczyna sie i konczy szukane slowo
    slowo_index = re.finditer('zmienilo',s)
    
    for slowo in slowo_index:
        ktory_index = slowo.span()
        print(ktory_index)
    #>>> slowo_w_tekscie_indexy()
    #(57, 65)
