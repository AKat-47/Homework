"""
Напишите программу определяющую допуск ученика к зачету.
Программа должна запрашивать число учеников, затем у каждого ученика запрашивать балл за финальный тест
и в ответ печатать, допущен ли он (True или False) к зачету (необходимо набрать больше 50 баллов).

Ученикам без допуска должно печататься "Вы отчислены".

Выдачу допуска реализуй как функцию.
"""
def dopusk(b):
    if b <= 50:
        print('Вы отчислены')
    else:
        print('Допуск есть')


kol = int(input())
for i in range(kol):
    dopusk(int(input('Кол-во баллов за тест:')))