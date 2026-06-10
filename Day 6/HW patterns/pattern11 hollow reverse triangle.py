n=6

for i in range(n-1,-1,-1):
    if i==n-1:
        print(" "*(n-i)+"* "*n)
    elif i==0:
        print(" "*(n-i)+"*")
    else:
        print(" "*(n-i)+"*",end="")
        print(" "*(i*2-1)+"*")