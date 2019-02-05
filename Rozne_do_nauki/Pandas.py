import pandas as pd
import matplotlib.pyplot as plt
from  matplotlib import style


web = {'day' : [1,2,3,4,5,6], 'visitors' : [100,200,1000,500,300,800], 'bounce_rate' : [20,23,20,15,16,10]}

df = pd.DataFrame(web)
head = df.head(2)
tail = df.tail(3)
x = df.sum()
xdf = pd.DataFrame(x)

# print(df)
# print(head)
# print(tail)
# print(xdf)


df1 = pd.DataFrame({"HPI" : [80,90,70,100], "Int_rate" : [2,1,2,3], "IND_GDP" : [50,45,45,67]}, index = [2001,2002,2003,2004])
df2 = pd.DataFrame({"HPI" : [80,90,70,60], "Int_rate" : [2,5,2,3], "IND_GDP" : [50,45,45,67]}, index = [2005,2006,2007,2008])

print(df1)
print(df2)
# merge wybiera czesci wspolna
print(df1.merge(df2))
merge = pd.merge(df1, df2)
print(merge)

merge2 = pd.merge(df1, df2, on = 'IND_GDP')
print(merge2)

# join dolacza do pierwszej df podana druga df
df3 = pd.DataFrame({"Int_rate" : [2,1,2,3], "IND_GDP" : [50,45,45,67]}, index = [2001,2002,2003,2004])
df4 = pd.DataFrame({"Low_HPI" : [50,45,67,34], "Unemployment" : [1,3,5,6]}, index = [2001,2003,2004,2005])
join = df3.join(df4)
join2 = df4.join(df3)
print(join)
print(join2)

# zmiana indexu na inny - przyklad -> zamiana na index = day
web2 = {'day' : [1,2,3,4,5,6], 'visitors' : [100,200,1000,500,300,800], 'bounce_rate' : [20,23,20,15,16,10]}
df5 = pd.DataFrame(web2)
df5.set_index("day", inplace=True)
print(df5)


# zmiana nazwy kolumny
df6 = df5.rename(columns = {"visitors" : "nowa_nazwa_kolumny_USERS"})
print(df6)

# rysowanie wykresu, index jako os X, pozostałe kolumny na os Y
style.use("fivethirtyeight")
df1.plot()
plt.show()


# konkatenacja - powiazanie
df7 = pd.DataFrame({"HPI" : [80,85,188,85], "Int_rate" : [52,3,2,2], "USD_GDP_Thousands" : [50,55,65,55]}, index = [2001,2002,2003,2004])
df8 = pd.DataFrame({"HPI" : [80,285,88,85], "Int_rate" : [2,73,2,2], "USD_GDP_Thousands" : [50,55,65,55]}, index = [2005,2006,2007,2008])

Concat = pd.concat([df7,df8])
print(Concat)


# czytanie csv z pliku i zamiana na html, po zapisie otworzyc plik html w przegladarce, uwaga - csv rozdzielane przecinkami a liczby z kropkami!!!
waluty = pd.read_csv('C:\\DATA SCIENCE KURS\\waluty.csv', index_col=0)
waluty.to_html('moja_nazwa_strony.html')
print(waluty)

# rysowanie wykresu na danych z pliku - trend dla bezrobocia we wszystkich krajach, ustawiam jako index nazwe kraju czyli 2 kolumne
country = pd.read_csv('C:\\DATA SCIENCE KURS\\unemployment2.csv', index_col=1)
df9 = country.head(5)
# wymieniam index na pierwsza kolumne czyli kod kraju
df9 = df9.set_index(["Code"])
# wskazuje , ze chce miec w tabeli tylko kolumny 2010,2011
sd = df9.reindex(columns=['2010','2011'])
print(sd)
db = sd.diff(axis=1)
db.plot(kind = "bar")
plt.show()

'''
      HPI  Int_rate  IND_GDP
2001   80         2       50
2002   90         1       45
2003   70         2       45
2004  100         3       67
      HPI  Int_rate  IND_GDP
2005   80         2       50
2006   90         5       45
2007   70         2       45
2008   60         3       67
   HPI  Int_rate  IND_GDP
0   80         2       50
1   70         2       45
merge2 = pd.merge(df1, df2, on = 'HPI') - nie mozna zmergowac 60 z 100
   HPI  Int_rate_x  IND_GDP_x  Int_rate_y  IND_GDP_y
0   80           2         50           2         50
1   90           1         45           5         45
2   70           2         45           2         45

merge2 = pd.merge(df1, df2, on = 'Int_rate') - uwaga wartosci nieunikalne na mergowalen kolumnie!!! oraz nie mozna zmergowac 1 z 5
    HPI_x  Int_rate  IND_GDP_x  HPI_y  IND_GDP_y
0     80         2         50     80         50
1     80         2         50     70         45
2     70         2         45     80         50
3     70         2         45     70         45
4    100         3         67     60         67

merge2 = pd.merge(df1, df2, on = 'IND_GDP') - tutaj rowniez nieunikalne
   HPI_x  Int_rate_x  IND_GDP  HPI_y  Int_rate_y
0     80           2       50     80           2
1     90           1       45     90           5
2     90           1       45     70           2
3     70           2       45     90           5
4     70           2       45     70           2
5    100           3       67     60           3

join = df3.join(df4)
join2 = df4.join(df3)
      Int_rate  IND_GDP  Low_HPI  Unemployment
2001         2       50     50.0           1.0
2002         1       45      NaN           NaN
2003         2       45     45.0           3.0
2004         3       67     67.0           5.0
      Low_HPI  Unemployment  Int_rate  IND_GDP
2001       50             1       2.0     50.0
2003       45             3       2.0     45.0
2004       67             5       3.0     67.0
2005       34             6       NaN      NaN

df5.set_index("day", inplace=True)
     visitors  bounce_rate
day                       
1         100           20
2         200           23
3        1000           20
4         500           15
5         300           16
6         800           10

konkatenacja
Concat = pd.concat([df7,df8])

      HPI  Int_rate  USD_GDP_Thousands
2001   80         2                 50
2002   85         3                 55
2003   88         2                 65
2004   85         2                 55
2005   80         2                 50
2006   85         3                 55
2007   88         2                 65
2008   85         2                 55

waluty
                      Waluta       Kupno    Sprzedaz  Spread
Kraj                                                        
Szwajcaria       1 CHF (CHF)  3.6561 PLN  3.8823 PLN  6.00 %
EU               1 EUR (EUR)  4.1750 PLN  4.4332 PLN  6.00 %
USA              1 USD (USD)  3.6415 PLN  3.8667 PLN  6.00 %
Australia        1 AUD (AUD)  2.6008 PLN  2.7616 PLN  6.00 %
Bulgaria         1 BGN (BGN)  2.1347 PLN  2.2667 PLN  6.00 %
Kanada           1 CAD (CAD)  2.7800 PLN  2.9520 PLN  6.00 %
Chiny           1 CNY (CNY)*  0.5255 PLN  0.5580 PLN  6.00 %
Czechy           1 CZK (CZK)  0.1615 PLN  0.1714 PLN  5.95 %
Dania            1 DKK (DKK)  0.5596 PLN  0.5942 PLN  6.00 %
W. Brytania      1 GBP (GBP)  4.7486 PLN  5.0424 PLN  6.00 %
Wegry          100 HUF (HUF)  1.2896 PLN  1.3694 PLN  6.00 %
Indie        100 INR (INR)**  4.9628 PLN  5.2698 PLN  6.00 %
Japonia        100 JPY (JPY)  3.2371 PLN  3.4373 PLN  6.00 %
Norwegia         1 NOK (NOK)  0.4419 PLN  0.4692 PLN  5.99 %
Rumunia          1 RON (RON)  0.8944 PLN  0.9497 PLN  6.00 %
Rosja            1 RUB (RUB)  0.0556 PLN  0.0590 PLN  5.93 %
Szwecja          1 SEK (SEK)  0.4039 PLN  0.4288 PLN  5.98 %
Turcja           1 TRY (TRY)  0.6442 PLN  0.6840 PLN  5.99 %
RPA              1 ZAR (ZAR)  0.2533 PLN  0.2689 PLN  5.97 %

'''