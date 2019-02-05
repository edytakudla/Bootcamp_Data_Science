'''

    Przekonwertuj skalę ocen (2, 3, 3.5, 4, 4.5, 5) na listę float za pomocą inline for
    Użytkownik podaje oceny jako int lub float
    Jeżeli ocena jest na liście dopuszczalnych ocen, dodaje ją do dzienniczka
    Jeżeli wciśnięto sam Enter, oznacza to koniec wpisywania do dzienniczka
    Jeżeli wpisano cyfrę nie znajdującą się na liście dopuszczalnych ocen, wyświetl informację “Grade is not allowed” i dalej kontynuuj wpisywanie
    Na zakończenie wyświetl wyliczoną dla dzienniczka średnią arytmetyczną z ocen

'''

scale = (2, 3, 3.5, 4, 4.5, 5)
grades_list = []
for grade in scale:
    grades_list.append(float(grade))
print(grades_list)

user_grade = input('Podaj nową ocenę: ')
user_grades_list = []


while user_grade != '':
    if float(user_grade) in grades_list:
        user_grades_list.append(float(user_grade))
        user_grade = input('Podaj nową ocenę: ')
    else:
        print('Grade is not allowed')
        user_grade = input('Podaj nową ocenę: ')

print('lista ocen uzytkownika: ', user_grades_list)
average = sum(user_grades_list)/len(user_grades_list)
print(f'grades_average: {average}')
