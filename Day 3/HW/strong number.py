num=int(input("Enter a number :"))
temp=num
sum=0

while num!=0:
    digit=num%10
    fact=1
    for i in range(digit,0,-1):
        fact*=i
    sum+=fact
    num//=10

if sum == temp:
    print("Entered number is a Strong Number")
else:
    print("Entered number is not a Strong Number")

