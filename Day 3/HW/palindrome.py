num=int(input("Enter a number :"))
temp=num
rev_no=0

while(num!=0):
    digit=num%10
    rev_no=(rev_no*10)+digit
    num//=10

if temp==rev_no:
    print("Entered number is palindrome")
else:
    print("Entered number is not palindrome")
