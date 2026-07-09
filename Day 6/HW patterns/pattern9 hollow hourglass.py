
n = 11
mid = n // 2

for i in range(mid,-1,-1):

    if i == mid:
        print("* "*(mid + 1))

    elif i == 0:
        print(" "*(mid-i) +"*")

    else:
        print(" " *(mid-i) +"*", end="")
        print(" " *(i*2-1) +"*")


for i in range(1, mid+1):

    if i == mid:
        print("* "* (mid + 1))

    else:
        print(" "*(mid-i) +"*", end="")
        print(" "*(i*2-1) +"*")

'''
n = 6

for i in range(n):
    for j in range(n):
        if i == 0 or j == i or j == n - i - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


for i in range(n - 2, -1, -1):
    for j in range(n):
        if i == 0 or j == i or j == n - i - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
'''