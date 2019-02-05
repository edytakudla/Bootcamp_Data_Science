# Budujemy listę domen, które zwracają poszczególne zapytania i zliczamy ile wyników z jakiej domeny. czyli miedzy //oraz pierwszy slash / Na zasadzie:
# wp.pl 10
# onet.pl 8
# interia.pl 3
# itd
# Dla chcących więcej:
# - czeszemy pierwsze 5 stron dla każdego zapytania
# - składujemy wynik w zaprojektowanym do tego celu obiekcie (DTO)

from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse
from collections import Counter

# do wyszukiwania w google w zapytaniu musi byc plus a nie spacja
def convert_str_to_google_search_phrase(phrase):
    return phrase.replace(" ", "+")


phrases = [
'Mistrzostwa Świata w Piłce Nożnej 2018',
'Avicii',
'Wybory samorządowe 2018',
'Tomasz Mackiewicz',
'About You',
'Kora Jackowska',
'Korona królów',
'Kler',
'Nanga Parbat',
'Meghan Markle'
]

# chcemy stworzyc slownik {nazwa_domeny : ilosc_wystapien}
domain_counter = dict()
domain_list = list()

for phrase in phrases:
    r = requests.get(f"https://google.com/search?q={convert_str_to_google_search_phrase(phrase)}")

    # html parser potrzebny, zeby wskazac, ze to jest strona html
    soup = BeautifulSoup(r.text, features="html.parser")

    # na stronie html znalezlismy, ze wszystkie linki maja klase cite
    # for cite in soup.select('div > div > div > cite'):
    #     print(cite.text)
    #     print(urlparse(cite.text))


    for cite in soup.select('div.g > h3.r > a'):
        #print(cite.get("href")[7:])
        #print(urlparse(cite.get("href")[7:]).hostname)
        domain_name = urlparse(cite.get("href")[7:]).hostname
        domain_list.append(domain_name)

        if domain_name not in domain_counter:
            domain_counter[domain_name] = 1
        else:
            domain_counter[domain_name] = domain_counter[domain_name] + 1

print(domain_counter)
print(domain_list)
print(Counter(domain_list))



