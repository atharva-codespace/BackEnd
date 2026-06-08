gender = input("Enter Gender (M/F): ")
age = int(input("Enter Age: "))
height = float(input("Enter Height (in feet): "))

if gender == 'M' or gender == 'm':
    if age >= 20 and height >= 5.5:
        print("Candidate Selected")
    else:
        if age < 18:
            print("Candidate Deselected because age is less than 18")
        if height < 5.5:
            print("Candidate Deselected because height is less than 5.5 feet")

elif gender == 'F' or gender == 'f':
    if age >= 18 and height >= 5.0:
        print("Candidate Selected")
    else:
        if age < 18:
            print("Candidate Deselected because age is less than 18")
        if height < 5.0:
            print("Candidate Deselected because height is less than 5.0 feet")

else:
    print("Invalid Gender")