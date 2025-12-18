start = int(input("Start: "))
step = int(input("Step: "))

if start < 15:
    r = range(start, 15 + 1, +step)
else:
    r = range(start, 15 - 1, -step)
for i in r:
    print(i)

