user_id = input("Enter your UserID: ")
password = input("Enter your password: ")

if user_id == "admin":
    if password == "1234":
        print("Login Successful")
    else:
        print("Incorrect password")
        print("Login unsuccessful")
else:
    print("Incorrect userID")
    print("Login unsuccessful")


