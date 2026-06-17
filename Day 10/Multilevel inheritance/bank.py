class bank:
    def __init__(self,name,IFSC):
        self.name=name
        self.ifsc=IFSC

    def display1(self):
        print("Nme of the bank: ",self.name)
        print("IFSC code of bank: ",self.ifsc)        