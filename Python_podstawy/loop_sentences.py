'''

    Dany jest tekst przemównienia John F. Kennedy’ego “Moon Speech” wygłoszony na Rice Stadium

        We choose to go to the Moon. We choose to go to the Moon in this decade and do the other things. Not because they are easy, but because they are hard. Because that goal will serve to organize and measure the best of our energies and skills. Because that challenge is one that we are willing to accept. One we are unwilling to postpone. And one we intend to win

    Dla każdego zdania (zdania oddzielone są kropkami)
    Za pomocą funkcji len() policz ile jest wyrazów
    Wypisz na ekranie listę słowników o strukturze: zdanie (klucz) -> ilość wyrazów (wartość)
    Na końcu wypisz także ile jest zdań oraz ile słów i znaków naliczyliśmy łącznie

    lista słów: ['We', 'choose', 'to', 'go', 'to', 'the', 'Moon.', 'We', 'choose', 'to', 'go', 'to', 'the', 'Moon', 'in', 'this', 'decade', 'and', 'do', 'the', 'other', 'things.', 'Not', 'because', 'they', 'are', 'easy,', 'but', 'because', 'they', 'are', 'hard.', 'Because', 'that', 'goal', 'will', 'serve', 'to', 'organize', 'and', 'measure', 'the', 'best', 'of', 'our', 'energies', 'and', 'skills.', 'Because', 'that', 'challenge', 'is', 'one', 'that', 'we', 'are', 'willing', 'to', 'accept.', 'One', 'we', 'are', 'unwilling', 'to', 'postpone.', 'And', 'one', 'we', 'intend', 'to', 'win']
    ile słów w tekście: 71
    lista zdań:  ['We choose to go to the Moon', ' We choose to go to the Moon in this decade and do the other things', ' Not because they are easy, but because they are hard', ' Because that goal will serve to organize and measure the best of our energies and skills', ' Because that challenge is one that we are willing to accept', ' One we are unwilling to postpone', ' And one we intend to win']
    ile zdań: 7
    [{'We choose to go to the Moon': 27, 'We choose to go to the Moon in this decade and do the other things': 66, 'Not because they are easy, but because they are hard': 52, 'Because that goal will serve to organize and measure the best of our energies and skills': 88, 'Because that challenge is one that we are willing to accept': 59, 'One we are unwilling to postpone': 32, 'And one we intend to win': 24}]

    MA WYJŚĆ 7/71/348!!!!!!!!!!!!!!!!!!!!!! split strip
'''

text = 'We choose to go to the Moon. We choose to go to the Moon in this decade and do the other things. Not because they are easy, but because they are hard. Because that goal will serve to organize and measure the best of our energies and skills. Because that challenge is one that we are willing to accept. One we are unwilling to postpone. And one we intend to win'
chars_number = len(text)

words_list = text.split()
words_number = len(words_list)

sentences_list = text.split('. ')
sentences_number = len(sentences_list)

sentences_dict = {}
new_list = []

for sentence in sentences_list:
    chars_in_sent_number = len(sentence)
    sentences_dict.update({sentence : chars_in_sent_number})
    new_list.append({sentence : chars_in_sent_number})



print(f'chars_number: {chars_number}')
print(f'words_list: {words_list}')
print(f'words_number: {words_number}')
print(f'new_list:  {new_list}')
print(f'sentences_number: {sentences_number}')

