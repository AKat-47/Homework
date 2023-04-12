a = [int(i) for i in input().split()]
if sorted(a) == a:
    print('Yes')
else:
    print('No')