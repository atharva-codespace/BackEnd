import random
import time

class Login:

    def __init__(self, username, password):
        self.username = username
        self.__password = password

    def generate_otp(self):
        self.otp = random.randint(100, 999)
        self.start_time = time.time()

        print("\nYour OTP is:", self.otp)
        print("Valid for 30 seconds")

    def verify_otp(self):
        user_otp = int(input("Enter OTP: "))

        if time.time() - self.start_time > 30:
            print("OTP Expired!")
        elif user_otp == self.otp:
            print("OTP Verified")
            print("Login Successful")
        else:
            print("Wrong OTP")

    def login(self):
        username = input("Enter Username: ")
        password = int(input("Enter Password: "))

        if username == self.username and password == self.__password:
            self.generate_otp()
            self.verify_otp()
        else:
            print("Invalid Username or Password")


obj = Login("Atharva", 123)
obj.login()