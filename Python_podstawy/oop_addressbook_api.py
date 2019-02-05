class AddressBook:
    def __init__(self, kontakty=()):
        self.kontakty = kontakty
        self.lista = []


class Contact:
    def __init__(self, imie=None, nazwisko=None, adresy = ()):
        self.imie = imie
        self.nazwisko = nazwisko
        self.adresy = adresy

    def __str__(self):
        out = ''
        for adres in self.adresy:
            out += f'{adres} '
        return f'{self.imie} {self.nazwisko} {out}'


class Address:
    def __init__(self, ulica=None, kod=None, miasto=None, stan=None, panstwo=None):
        self.ulica = ulica
        self.kod = kod
        self.miasto = miasto
        self.stan = stan
        self.panstwo = panstwo

    def __str__(self):
        return str(self.miasto)

    def __repr__(self):
        return self.__repr__()


melissa = Contact(imie='Melissa', nazwisko='Lewis')
print(melissa)
# Melissa Lewis

mark = Contact(imie='Mark', nazwisko='Watney', adresy=[Address(miasto='Houston'), Address(miasto='Cocoa Beach')])
print(mark)
# Mark Watney [Houston, Cocoa Beach]

addressbook = AddressBook([
    Contact(imie='Matt', nazwisko='Kowalski', adresy=[
        Address(ulica='2101 E NASA Pkwy', miasto='Houston', stan='Texas', kod='77058', panstwo='USA'),
        Address(ulica=None, miasto='Kennedy Space Center', kod='32899', panstwo='USA'),
        Address(ulica='4800 Oak Grove Dr', miasto='Pasadena', kod='91109', panstwo='USA'),
        Address(ulica='2825 E Ave P', miasto='Palmdale', stan='California', kod='93550', panstwo='USA'),
    ]),
    Contact(imie='José', nazwisko='Jiménez'),
    Contact(imie='Иван', nazwisko='Иванович', adresy=[]),
])


print(addressbook)
# [Matt Kowalski [Houston, Kennedy Space Center, Pasadena, Palmdale], José Jiménez, Иван Иванович]
