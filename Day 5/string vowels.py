str = input("Enter a string: ")

vowels = "AEIOUaeiou"

print("The vowels present in the string are:")

for ch in str:
    if ch in vowels:
        print(ch, end=" ")