"""
Каждый стажёр мог выбрать любое число предметов для изучения. По каждому предмету он мог набрать от 0 до 50 баллов.

Программа должна:
Пока пользователь не введет "стоп"":
1. Запрашивать имя студента и число предметов.
2. Запрашивать число баллов по каждому предмету и печатать общую сумму баллов: «Итоговый счёт: _».
3. По сумме баллов опеределять тип грамоты о прохождении стажировки:
- баллов больше 80 — «Наградить дипломом.»;
- баллов больше 50 и меньше или равно 80 — «Наградить похвальной грамотой.»;
- остальные случаи — «Выдать грамоту об участии.».
"""
def gramota(k):
    if k > 80:
        return 'Наградить диплом'
    elif k > 50:
        return 'Наградить похвальонй грамотой'
    else:
        return 'Выдать грамоту об участии'


name = input('Введите имя: ')
while name != 'стоп':
    predm = int(input('Введите количество предметов: '))
    s = 0
    for i in range(predm):
        a = int(input('Количество баллов: '))
        s += a
    print(gramota(s))
    name = input('Введите имя: ')