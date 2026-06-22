from B import B
from C import C

class D(B, C):
    def show(self):
        print("Method show() from Class D")

    def __init__(self, name, age, price, qty):
        print("=" * 35)
        print("      PRODUCT DETAILS")
        print("=" * 35)

        B.__init__(self, name, age)
        C.__init__(self, price)

        self.qty = qty
        print(f"Qty   : {self.qty}")

        print("=" * 35)

obj = D("Raj", 30, 2000, 5)