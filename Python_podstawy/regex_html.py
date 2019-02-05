import re
'''
with open('moon-speech.html') as file:
    zawartosc = file.read()

pattern = r"<p>(We choose to go to the moon.*?)</p>"

matchlist = re.findall(pattern, zawartosc)
print(matchlist)
'''

# drugi sposob z zajec
paragraphs = re.compile(r'<p>(.*?)</p>')    #lista paragrafow


with open('moon-speech.html') as file:
    TEXT = file.read()

for p in paragraphs.findall(TEXT):
    if p.startswith('We choose'):
        print(p)
