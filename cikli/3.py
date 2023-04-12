log = input('Введите логин: ')
a = []
f = True
for i in log:
    if i in '=?*^$№@_ ':
        a.append(i)
        f = False
if f:
    print('Логин верный')
else:
    print('Уберите символы:', a)