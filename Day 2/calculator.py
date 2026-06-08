choice = 1

while choice != 6:

    print("\n----- CALCULATOR -----")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 6:
        print("Thank You!")
        break

    elif choice < 1 or choice > 6:
        print("Invalid Choice")
        continue

    a = float(input("Enter 1st number: "))
    b = float(input("Enter 2nd number: "))

    match choice:

        case 1:
            print(f"Addition of {a} and {b} = {a + b}")

        case 2:
            print(f"Subtraction of {a} and {b} = {a - b}")

        case 3:
            print(f"Multiplication of {a} and {b} = {a * b}")

        case 4:
            if b != 0:
                print(f"Division of {a} and {b} = {a / b}")
            else:
                print("Division by zero is not possible")

        case 5:
            if b != 0:
                print(f"Modulus of {a} and {b} = {a % b}")
            else:
                print("Modulus by zero is not possible")