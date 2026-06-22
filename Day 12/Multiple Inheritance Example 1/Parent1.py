class p1:
    def __init__(self,name):
        self.name=name
        print("p1 const")
        print("From parent1 ",self.name)
    def xyz(self):
        print("From p1 XYZ")
    def show(self):
        print("from p1 show")