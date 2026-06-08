str = input("Enter a string: ")

rev_str = ""

for i in range(len(str)-1, -1, -1):
    rev_str += str[i]

if str == rev_str:
    print("Entered string is palindrome")
else:
    print("Entered string is not palindrome")