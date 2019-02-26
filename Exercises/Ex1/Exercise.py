# This Python file uses the following encoding: utf-8

passports = {'0': ['Иванов', 1971],
       '1': ['Петров', 1985],
       '2': ['Козлов', 1988],
       '3': ['Васильев', 1990],
       '4': ['Кольцов', 1975],
       '5': ['Сидорова', 1981],
       '6': ['Лаврушкина', 1989],
       '7': ['Травкин', 1965]}
passport = str(input("Введите номер паспорта: "))
x = passport
person = str(passports[x][0]) + ' ' + str(passports[x][1])
print('Человек: ' + person)
