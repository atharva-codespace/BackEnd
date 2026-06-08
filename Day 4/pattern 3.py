count = 1

for i in range(1, 6):
    if i % 2 != 0:
        for j in range(count):
            print(i, end=" ")
        print()
        count += 1