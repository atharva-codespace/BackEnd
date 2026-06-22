from Payment import payment
from Product import product

class order(payment,product):
    def bill(self):
        qty=int(input("Enter quantity:"))
        self.total=self.price*qty
        print(self.show_product())
        print(self.pay(self.total))
        

obj=order("car",5000)
obj.bill()
