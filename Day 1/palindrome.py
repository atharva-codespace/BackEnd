a=int(input("Enter the number:"))
temp=a
rev_no=0


while a!=0:
    digit=a%10
    rev_no=(rev_no*10)+digit
    a//=10

print(rev_no)

if temp == rev_no:
    print("Entered number is a palindrome")
else:
    print("Entered number is not a palindrome")
