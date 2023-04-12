s = int(input())
time = int(input('введите время в формате: <час>:<минуты> ')[:2])
if (time > 22) or (time < 8):
    print('Магазин не работает')
else:
    if (time >= 10) and (time < 12):
        print(s / 2)
    elif (time >= 20) and (time < 22):
        print(s / 4)
    else:
        print(s)
