n=7

for i in range(n//2+1):
    for j in range(i+1):
        print("*",end="")
    print()

for i in range(n//2,0,-1):
    for j in range(i):
        print("*",end="")
    print()