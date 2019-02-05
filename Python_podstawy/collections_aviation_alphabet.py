'''

    Stwórz słownik języka pilotów
    Pojedynczym literom przyporządkuj ich fonetyczne odpowiedniki
    Do przekonwertowania tabelki poniżej, wykorzystaj zaznaczanie wielu linijek za pomocą klawisza alt w Twoim IDE
    Wczytaj od użytkownika literę
    Użytkownik zawsze poda przynajmniej jedną literę, cyfrę lub znak specjalny
    Wypisz na ekranie nazwę fonetyczną litery
    Jeżeli użytkownik podał więcej niż jedną literę, to wybierz z ciągu tylko pierwszą
    Słownik ma wyświetlić kod bez względu na to czy użytkownik podał dużą czy małą literę
    Jeżeli wpisał znak, k†óry nie jest w alfabecie, to wypisz “Pilots don’t say that”
    Nie używaj konstrukcji if, ani try i except

'''
pilot_dict = {'A': 'Alfa',
'B': 'Bravo',
'C': 'Charlie',
'D': 'Delta',
'E': 'Echo',
'F': 'Foxtrot',
'G': 'Golf',
'H': 'Hotel',
'I': 'India',
'J': 'Juliet',
'K': 'Kilo',
'L': 'Lima',
'M': 'Mike',
'N': 'November',
'O': 'Oscar',
'P': 'Papa',
'Q': 'Quebec',
'R': 'Romeo',
'S': 'Sierra',
'T': 'Tango',
'U': 'Uniform',
'V': 'Victor',
'W': 'Whisky',
'X': 'X-Ray',
'Z': 'Zulu'}

print(pilot_dict)
letter = (input('podaj litere: ')).upper()
print(f'pierwszy znak to {letter[0]}')
# uzycie get - sprawdz 1 znak, jesli nie ma to wyswietl tekst
print(pilot_dict.get(letter[0], "Pilots don’t say that"))

