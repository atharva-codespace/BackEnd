num=int(input("Enter a number :"))
sum=0

while num!=1 and num!=4:
    sum=0
    while num!=0:
        digit=num%10
        sum+=digit*digit
        num//=10
    num=sum

if num == 1:
    print("Entered number is a Happy Number")
else:
    print("Entered number is not a Happy Number")