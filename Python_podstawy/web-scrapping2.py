from bs4 import BeautifulSoup
import requests

# r = requests.get("https://wp.pl")
r = requests.get("https://stackoverflow.com")

data = r.text
data2 = r.links

soup = BeautifulSoup(data)

# wyszukanie linków na stronie wp.pl

# for link in soup.find_all('a class="question-hyperlink" '):
    #print(link.get('href'))

# chcemy pozyskac liste pytan ze strony stackover...
# Javafx use ObservableList for more than one ComboBox
# How to laravel validate to input only numbers and letters a-z and A-Z with space?
# Laravel mail error: Process could not be started [The system cannot find the path specified. ]
# Java game programming - keep player within playing field & avoiding certain obstacles


for link in soup.find_all("a", {"class": "question-hyperlink"}):
    print(link.text.strip())

 # szukanie po selektorach
 # soup.select("p > a")     # sprawdzić wołanie po selectach, tutaj select elementy a, ktore znajduja sie poniżej paragrafu p, a dziedziczy z p




