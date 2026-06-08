num = int(input("Enter a number: "))

if num < 2:
    print("Entered number is not Prime number")
else:
    count = 0

    for i in range(1, num + 1):
        if num % i == 0:
            count += 1

    if count == 2:
        print("Entered number is Prime number")
    else:
        print("Entered number is not Prime number")