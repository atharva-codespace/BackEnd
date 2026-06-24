class payment:
    def pay(self):
        pass
    print("Payment Process Started...")

class upi(payment):
    def pay(self):
        return "Payment done by UPI"
    
class gpay(payment):
    def pay(self):
        return "Payment done by GPay"
    
class payment_module:
    def payment_process(self,obj):
        print(obj.pay())

p=payment_module()
print("Payment:")
print("1.UPI\n2.GPay\n3.Card\n4.Exit")
ch=int(input("Enter your choice:"))
match ch:
    case 1:
        obj=upi()
    case 2:
        obj=gpay()
    case 3:
        pass
    case 4:
        print("Exiting..")
    case _:
        print("Invalid Choice...")
p.payment_process(obj)

#obj=[upi(),gpay()]
#for i in obj:
#    print(i.pay())