a=int(input("Enter the number:"))

rev_no=0
digit=0

while a!=0:
    digit=a%10
    rev_no=(rev_no*10)+digit
    a//=10

print(rev_no)

'''
rev=a[::-1]
print(rev)
'''