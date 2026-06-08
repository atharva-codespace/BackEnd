a=int(input("Enter the starting no.:"))
b=int(input("Enter the ending no.:"))

for i in range(a,b,1):
    if i %12==0 and i%6 ==0:
        print(i)
