a=int(input("Enter 1st no:"))
b=int(input("Enter 2nd no:"))
c=int(input("Enter 3rd no:"))

if a>=b and a>=c:
    print(f"{a} is the greatest number")
elif b>=c:
    print(f"{b} is the greatest number")
else:
    print(f"{c} is the greatest number")