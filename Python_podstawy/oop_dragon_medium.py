"""
    Zaimportuj smoka z zadania podstawowego
    Wykorzystaj mechanizm dziedziczenia dla Smoka
    Smok nie może wyjść poza obszar ekranu (1024x768) + napis doctest
    Jeżeli dojdzie do granicy ekranu, to przesuwając dalej, pozycja będzie ustawiona na maks
    Zmień smokowi punkty życia na losowy int z zakresu 100 do 150

    Stwórz bohatera (José Jiménez):

            losowe punkty życia (200-250)
            zadaje losowe obrażenia (1-15)
            klasa postaci (domyślnie “Warrior”)

    Wszystkie istoty mają statusy:

            “Full Health” - gdy punkty życia 100% (zastąp status “alive”)
            “Injured” - gdy punkty życia 99% - 75%
            “Badly Wounded” - gdy punkty życia 75% - 25%
            “Near Death” - gdy punkty życia poniżej 25%

    Bohater przejmuje złoto smoka, jeżeli go zabije

    Przeprowadź walkę, tak długo aż ktoś pierwszy nie zginie

"""

from oop_dragon_easy import Dragon
import random


def define_state(current_life_points):
    percent = current_life_points/(oop_dragon_easy.Dragon.life_points)
    if (percent == 1):
        another_state = 'Full Health'
    if (percent >= 0.75 and percent < 1):
        another_state = 'Injured'
    if (percent >= 0.25 and percent < 0.75):
        another_state = 'Badly Wounded'
    if (percent > 0 and percent < 0.25):
        another_state = 'Near Death'
    else:
        another_state = 'Dead'



    def __init__(self,another_state):
        super().__init__(self, name, x, y, texture, life_points, state)
        self.another_state = another_state

    #def receive_damages_dragon(self,points):


class Hero:
    def __init__(self, name, surname, hero_life_points=random.randint(200,251), hero_class='Warrior'):
        self.name = name
        self.surname = surname
        self.hero_life_points = hero_life_points
        self.hero_class = hero_class

    #def receive_damages_hero(self,points):

jose = Hero('Jose','Jimenez')
print(jose.name, jose.surname, jose.hero_life_points, jose.hero_class)

