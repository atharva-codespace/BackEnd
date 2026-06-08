num=int(input("Enter a number :"))
temp=num
count=0
sum=0

while temp!=0:
    count+=1
    temp//=10

temp=num

while num!=0:
    digit=num%10
    sum+=pow(digit,count)
    num//=10

if temp==sum:
    print("Entered number is Armstrong number")
else:
    print("Entered number is not Armstrong number")

