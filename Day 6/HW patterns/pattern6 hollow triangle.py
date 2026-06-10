n = 6

for i in range(n):

    if i == 0:
        print(" "*(n-i) + "*")

    elif i == n-1:
        print(" "*(n-i)+"* " * n)

    else:
        print(" "*(n-i) + "*", end="")
        print(" "*(i*2-1) + "*")