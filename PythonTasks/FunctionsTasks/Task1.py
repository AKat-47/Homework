"""
Напишите программу печатающую бейджики учеников.
Программа запрашивает ввод числа учеников и печатает каждому бейджик. Бейдж содержит название учебного заведения:
«Колледж Сириус», поле для имени:
«Имя: ____» и поле для школы:
«Группа: ____». Напиши программу, печатающую бейджики студентов как на картинке. В завершении программа должна печатать:
«Готово! Заберите бейджики.»
Функция должна принимать имя и группу ученика.
"""


def bey(n, gr):
    print('«Колледж Сириус»')
    print('Имя: ', n)
    print('Группа: ', gr)


name = input('Введите имя(завершение = 0) ')
while name != '0':
    group = input('номер группы: ')
    bey(name, group)
    name = input('Введите имя(завершение = 0) ')
print('Готово! Заберите бейджики.')
