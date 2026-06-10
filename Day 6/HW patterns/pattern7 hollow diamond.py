n = 11


for i in range(n//2 + 1):

    if i == 0:
        print(" "*(n//2-i) + "*")

    else:
        print(" "*(n//2-i) + "*", end="")
        print(" "*(i*2-1) + "*")


for i in range(n//2-1, -1, -1):

    if i == 0:
        print(" "*(n//2-i) + "*")

    else:
        print(" "*(n//2-i) + "*", end="")
        print(" "*(i*2-1) + "*")