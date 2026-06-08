lis = [21, 32, 65, 25, 5]

for i in range(len(lis)):

    if lis[i] % 2 == 0:
        lis[i] = 0
    else:
        lis[i] = 1

print("Updated list is:", lis)