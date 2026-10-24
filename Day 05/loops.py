max = 101

y = max
total = 0
for x in range(1, max):
    y -= 1
    total += x

    print(x, y)
    print(x + y)

print("The total is:", total)