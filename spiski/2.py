mark = [2, 4, 5, 3, 2, 3]
t, f, fv = mark.count(3), mark.count(4), mark.count(4)
for i in range(2, 6):
    print(i, ': ', mark.count(i))
print('marks: ', *mark)
print(round((t + f + fv) / len(mark) * 100, 2))