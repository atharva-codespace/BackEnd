ch = input("Enter any character: ")

if 'A' <= ch <= 'Z':
    print("Capital Letter")
elif 'a' <= ch <= 'z':
    print("Small Letter")
elif '0' <= ch <= '9':
    print("Number")
else:
    print("Special Symbol")