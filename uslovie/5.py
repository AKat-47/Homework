num = int(input())
s = 0
if (int(str(num)[-1]) % 2 == 0) and (sum([int(i) for i in str(num)]) % 3 == 0):
    print('делится')
else:
    print('не делится')