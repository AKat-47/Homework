name = input()
lst = []
while name != '0':
    if name not in lst:
        lst.append(name)
    else:
        print('Эта игра уже записана')
    name = input()
a = sorted(lst)
print(a)
