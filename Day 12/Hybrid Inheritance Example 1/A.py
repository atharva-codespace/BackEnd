class A:
    def xyz(self):
        print("Method xyz() from Class A")

    def __init__(self, name):
        self.name = name
        print(f"Name  : {self.name}")