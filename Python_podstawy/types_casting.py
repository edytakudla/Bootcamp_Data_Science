# PRAWIDŁOWO!!!

meters = 1337
km = int(meters/1000)
miles = float(meters/1608)
nm = float(meters/1852)

print(f'Meters: {meters}')                    # int
print(f'Kilometers: {km}')                # int
print(f'Miles: {miles}')                     # float
print(f'Nautical Miles: {nm}')            # float
print(f'All: {meters}, {km}, {miles}, {nm}')  # int, int, float, float


# TAK NIE UŻYWAĆ!!!

print(f'Meters: {1337}')                    # int
print(f'Kilometers: {int(1337/1000)}')                # int
print('Kilometers:',int(1337/1000))                # int
print(f'Miles: {float(1337/1608)}')                     # float
print(f'Nautical Miles: {float(1337/1852)}')            # float
print(f'All: {1337}, {int(1337/1000)}, {float(1337/1608)}, {float(1337/1852)}')  # int, int, float, float

age = 30
print(f'My age is: {age}') # literka f powoduje podstawienie wartości w klamrach, bez f wydrukuje sie string