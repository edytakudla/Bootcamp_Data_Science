class Ksiazka:
    def __init__(self):
        self.lista_kontaktow = []

    def dodaj_kontakt(self,kontakt):
        self.lista_kontaktow.append(kontakt)


class Kontakt:
    def __init__(self, imie=None, nazwisko=None, adres=[]):
        self.imie = imie
        self.nazwisko = nazwisko
        self.adres = adres

    def dodaj_adres(self, adres):
        self.lista_adresow.append(adres)

    def __str__(self):
        return(f'imie: {self.imie}, nazwisko: {self.nazwisko}')

class Adres:
    def __init__(self, ulica=None, kod=None, miasto=None, stan=None, kraj=None):            # tutaj None ozn. nieobowiazkowe, domyslnie nie podano, mozna tez uzywac ''
        self.ulica = ulica
        self.kod = kod
        self.miasto = miasto
        self.stan = stan
        self.kraj = kraj

    def __str__(self):
        return(f'ulica: {self.ulica}, kod: {self.kod}, miasto: {self.miasto}, stan: {self.stan}, kraj: {self.kraj}')

jose = Kontakt(imie='Jose',nazwisko='Jimenez')
adres1 = Adres(ulica='2101 E NASA Pkwy', kod='77058', miasto='Houston', stan='Texas', kraj='USA')
adres2 = Adres(ulica='Kennedy Space Center', kod='32899', stan='Florida', kraj='USA')
jose.adres.append(adres2)
ksiazka = Ksiazka()
ksiazka.dodaj_kontakt(jose)

print(jose)
print(adres1)

mark = Kontakt('Mark','Watney')
ksiazka_adresowa = Ksiazka()
ksiazka_adresowa.dodaj_kontakt(jose)
ksiazka_adresowa.dodaj_kontakt(mark)
print(ksiazka_adresowa)