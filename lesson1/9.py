n = int(input())
print(int(str(n % 10) + str((n // 10) % 10) + str(n // 100)))