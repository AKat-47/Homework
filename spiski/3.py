marks = [int(i) for i in input().split()]
five = marks.count(5)
print(five / len(marks) * 100)