a, b, c = [int(input()) for i in range(3)]
if (a < b) and (b < c):
    print('Акция!', 'К оплате:', (a + b + c) / 2)
elif (a > b) and (b > c):
    print('Акция!', 'К оплате:', (a + b + c) / 3)
else:
    print('К оплате:', a + b + c)
