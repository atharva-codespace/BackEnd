from A import A

class C(A):
    def pqr(self):
        print("Method pqr() from Class C")

    def __init__(self, price):
        print("Initializing Class C")
        self.price = price
        print(f"Price : ₹{self.price}")