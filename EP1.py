x = 3
y = 0
Number = (8456)

for x in range(0,Number):
    z = x%3
    a = x%5
    if z == 0:
        y=y+x

    elif a == 0:
        y = y + x
    x = x + 1

print(y)