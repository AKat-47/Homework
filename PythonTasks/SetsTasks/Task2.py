"""
Имеется список с произвольными значениями. Нужно преобразовать его во множество и проверить
являются ли все его элементы неизменяемыми.
Вывести True или False. И изменяемые элементы
Подсказка: чтобы узнать тип элемента можно использовать функцию type()
"""
testList = [1, 2, 2, [3, 4], (1, 2, 3), "1", {1, 2, 3}]
printSet = set()
flag = True
for i in testList:
    if type(i) not in [list, set, dict]:
        printSet.add(i)
    else:
        flag = False
        print('изменяется', i)
print(flag, ', ', printSet)

