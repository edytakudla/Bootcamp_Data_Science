"""
2.4.1. Dragon (Easy)

    Smok ma mieć:

            nazwę smoka
            pozycja x na ekranie
            pozycja y na ekranie
            teksturę, domyślnie dragon.png
            punkty życia, domyślnie losowy int z zakresu od 50 do 100

    Smok może:

            otrzymywać obrażenia
            zadawać komuś losowe obrażenia z przedziału od 5 do 20
            być ustawiony w dowolne miejsce ekranu
            być przesuwany o zadaną liczbę punktów w którymś z kierunków

    Przyjmij górny lewy róg ekranu za punkt (0, 0)

            idąc w prawo dodajesz x
            idąc w lewo odejmujesz x
            idąc w górę odejmujesz y
            idąc w dół dodajesz y

    Przy każdym obrażeniu wypisz na ekranie nazwę smoka, ilość obrażeń i pozostałe punkty życia

    Kiedy punkty życia smoka spadną do, lub poniżej zera:

            ustaw status obiektu na dead
            na ekranie ma pojawić się napis ‘XXX is dead’ gdzie XXX to nazwa smoka
            zmień teksturę smoka na dragon-dead.png
            na ekranie pojawi się informacja ile złota smok wyrzucił (losowa 1-100)
            na ekranie pojawi się informacja o pozycji gdzie smok zginął

    Nie można zadawać smokowi obrażeń, jeżeli już nie żyje

    Przeprowadź grę:

            Stwórz smoka w pozycji x=50, y=120 i nazwij go Wawelski
            Ustaw nową pozycję na x=10, y=20
            Przesuń smoka o 10 w lewo i 20 w dół
            Przesuń smoka o 10 w lewo i 15 w prawo
            Przesuń smoka o 15 w prawo i 5 w górę
            Przesuń smoka o 5 w dół
            Zadaj 10 obrażeń smokowi
            Zadaj 5 obrażeń smokowi
            Zadaj 3 obrażeń smokowi
            Zadaj 2 obrażeń smokowi
            Zadaj 15 obrażeń smokowi
            Zadaj 25 obrażeń smokowi
            Zadaj 75 obrażeń smokowi

    Jeżeli konieczne jest wprowadzenie nowej metody, klasy lub pól to należy to zrobić

"""

import random

class Dragon:
    def __init__(self, name=None, x=0, y=0, texture='dragon.png', life_points=random.randint(50,101), state = 'not_dead'):
        self.name = name
        self.x = x
        self.y = y
        self.texture = texture
        self.life_points = life_points
        self.state = state


    def receive_damages(self, points):
        self.life_points = self.life_points - points

        # zmiana stanu smoka
        if self.life_points <= 0:
            self.state = 'dead'
            self.texture = 'dragon-dead.png'
            print(f'{self.name} is dead, smok wyrzucil zlota {random.randint(1,101)}, zginal na pozycji {self.x} {self.y}')
        else:
            self.state = 'not_dead'

        print(f'atak na smoka!! name = {self.name}, points = {self.life_points}, life_points = {self.life_points}, state = {self.state}')


    def hurt_somebody(self, hurt_points=random.randint(5,20)):
        pass
        # smok zadaje obrazenia innym

    def go_to_new_position(self, x1, y1):
        self.x1 = x1
        self.y1 = y1
        self.x = self.x + x1
        self.y = self.y + y1
        # nowa pozycja smoka po przesunieciu o x1 i y1

#if __name__ == '__main__':

# Stwórz smoka w pozycji x=50, y=120 i nazwij go Wawelski
wawelski = Dragon(name='Wawelski', x=50, y=120)
print('DRAGON - start: ',wawelski.name, wawelski.x, wawelski.y, wawelski.life_points, wawelski.texture, wawelski.state)
# Ustaw nową pozycję na x=10, y=20
wawelski.x=10
wawelski.y=20
print('DRAGON - zmiana pozycji startowej: ',wawelski.name, wawelski.x, wawelski.y, wawelski.life_points, wawelski.texture, wawelski.state)
# Przesuń smoka o 10 w lewo i 20 w dół
wawelski.go_to_new_position(10,20)
print('DRAGON: ',wawelski.name, wawelski.x, wawelski.y, wawelski.life_points, wawelski.texture, wawelski.state)
# Przesuń smoka o 10 w lewo
wawelski.go_to_new_position(-10,0)
print('DRAGON: ',wawelski.name, wawelski.x, wawelski.y, wawelski.life_points, wawelski.texture, wawelski.state)
#  i 15 w prawo
wawelski.go_to_new_position(15,0)
print('DRAGON: ',wawelski.name, wawelski.x, wawelski.y, wawelski.life_points, wawelski.texture, wawelski.state)
# Przesuń smoka o 15 w prawo
wawelski.go_to_new_position(15,0)
print('DRAGON: ',wawelski.name, wawelski.x, wawelski.y, wawelski.life_points, wawelski.texture, wawelski.state)
# i 5 w górę
wawelski.go_to_new_position(0,-5)
print('DRAGON: ',wawelski.name, wawelski.x, wawelski.y, wawelski.life_points, wawelski.texture, wawelski.state)
# Przesuń smoka o 5 w dół
wawelski.go_to_new_position(0,5)
print('DRAGON: ',wawelski.name, wawelski.x, wawelski.y, wawelski.life_points, wawelski.texture, wawelski.state)
# Zadaj 10 obrażeń smokowi
wawelski.receive_damages(10)
wawelski.receive_damages(5)
wawelski.receive_damages(3)
wawelski.receive_damages(2)
wawelski.receive_damages(15)
wawelski.receive_damages(25)
wawelski.receive_damages(75)
print('DRAGON: ',wawelski.name, wawelski.x, wawelski.y, wawelski.life_points, wawelski.texture, wawelski.state)
