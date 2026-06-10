n = 9

mid = n // 2

for i in range(n):

    if i == 0 or i == mid or i == n-1:
        print("*" * n)

    elif i < mid:
        print("*")

    else:
        print(" " * (n-1) + "*")