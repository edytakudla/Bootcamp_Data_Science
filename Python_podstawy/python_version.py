import sys
import os
from testy_rozne import test

# jaka wersja pythona
print(f'Version: {sys.version}')

# gdzie jest zainstalowany
print(f'Installation: {sys.executable}')

print(f'Virtualenv: {os.getenv("VIRTUAL_ENV")}')

test.sumuj_liczby(5, 10)
test.name()


