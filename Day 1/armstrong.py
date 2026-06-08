num=int(input("Enter a number:"))
temp=num
sum=0
digit=0

while temp != 0:
    digit+=1
    temp//=10
#digits = len(str(num))

temp=num
while num!=0:
    di=num %10
    sum+=pow(di,digit)
    num//=10

if temp==sum:
    print("Entered number is Armstrong number")
else:
    print("Entered number is not Armstrong number")

