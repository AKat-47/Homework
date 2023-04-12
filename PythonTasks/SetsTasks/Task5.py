"""
Каждый из N школьников некоторой школы знает M языков.
Определите, какие языки знают все школьники и языки, которые знает хотя бы один из школьников.
Входные данные:
Сначала запрашивается количество учеников(например 6).
Дальше запрашивается количество учеников знающих определенный набор языков и языки которые они знают
Например:
3
Russian
English
Japanese
2
Russian
English
1
English
Вывод должен быть:
3 - [Russian, English,Japenese]
1 - [English]
"""
n = int(input('Введите количество учеников(чтобы закончить введите 0): '))
levery = set()
lall = set()
f = True
while n != 0:
    lt = set()
    for i in range(n):
        lang = input('Введите язык: ')
        lall.add(lang)
        lt.add(lang)
    if f:
        levery = lt
    else:
        levery = levery & lt
    n = int(input('Введите количество учеников(чтобы закончить введите 0): '))
print(len(lall), '-', lall)
print(len(levery), '-', levery)


