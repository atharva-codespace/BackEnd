from bank import bank

class account(bank):
    def __init__(self, name, IFSC,acc_no,acc_hold):
        super().__init__(name, IFSC)
        self.acc_no=acc_no
        self.acc_hold=acc_hold

    def display2(self):
        super().display1()
        print("Account no: ",self.acc_no)
        print("Account Holder: ",self.acc_hold)


        
