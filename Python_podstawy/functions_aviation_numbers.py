'''

    Napisz funkcję number_to_str
    Funkcja zamieni dowolnego int lub float na formę tekstową w mowie pilotów

Tab. 14.1. Aviation Phonetic Numbers Letter 	Pronounce
0 	Zero
1 	One
2 	Two
3 	Tree
4 	Fower
5 	Fife
6 	Six
7 	Seven
8 	Ait
9 	Niner

number_to_str(1969)       # 'one niner six niner'
number_to_str(31337)      # 'tree one tree tree seven'
number_to_str(13.37)      # 'one tree and tree seven'
number_to_str(31.337)     # 'tree one and tree tree seven'
number_to_str(-1969)      # 'minus one niner six niner'
number_to_str(-31.337)    # 'minus tree one and tree tree seven
number_to_str(-49.35)     # 'minus fower niner and tree fife'

'''

def number_to_str(number):
    '''
    >>> number_to_str(31)
    tree one
    '''

    strings = {
    '0':	'Zero',
    '1':	'One',
    '2':	'Two',
    '3':	'Tree',
    '4':	'Fower',
    '5':	'Fife',
    '6':	'Six',
    '7':	'Seven',
    '8':	'Ait',
    '9':    'Niner',
    '-':    'minus',
    '.':    'and',

    }


    str_num = str(number)

# SPOSOB 1 - POPRZEZ STRING
    s = ''
    for elem in str_num:
        s = s + strings[elem].lower() + ' '

    print(f'poprzez stringi: {s}')


# SPOSOB 2 - POPRZEZ LISTE

    list = []
    t = '***'
    for elem in str_num:
        list.append(strings[elem].lower())
    t = t.join(list)
    print(f'poprzez liste oraz join: {t}')


number_to_str(196966666)
number_to_str(31337)
number_to_str(13.37)
number_to_str(31.337)
number_to_str(-1969)
number_to_str(-31.337)
number_to_str(-49.35)