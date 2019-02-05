a = 'UL. Jana III Sobieskiego 1/2'
b = 'ulica Jana III Sobieskiego 1/2'
c = 'os. Jana III Sobieskiego 1/2'
d = 'plac Jana III Sobieskiego 1/2'
e = 'aleja Jana III Sobieskiego 1/2'
f = 'alei Jana III Sobieskiego 1/2'
g = 'Jana III Sobieskiego 1 m. 2'
h = 'os. Jana III Sobieskiego 1 apt 2'

list = [a,b,c,d,e,f,g,h]
print(list)

print(a[4:24])
print(b[6:26])
print(c[4:24])
print(d[5:25])
print(e[6:26])
print(f[5:25])
print(g[:20])
print(h[4:24])

print(a[::-1])
print(a[::-2])
print(a[::2])

start_index = a.find('J')
end_index = start_index + 20
print(start_index, end_index)
print(a[start_index:end_index])


for item in list:
    start_index = item.find('J')
    end_index = start_index + 20

    print('z petli: ', item[start_index:end_index])