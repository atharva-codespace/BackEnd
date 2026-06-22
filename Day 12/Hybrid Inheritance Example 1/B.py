from A import A

class B(A):
    def abc(self):
        print("Method abc() from Class B")

    def __init__(self, name, age):
        print("\nInitializing Class B")
        A.__init__(self, name)
        self.age = age
        print(f"Age   : {self.age}")