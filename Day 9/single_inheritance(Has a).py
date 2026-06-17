class Engine:
    def __init__(self, chassis_no, horsepower):
        self.chassis_no = chassis_no
        self.horsepower = horsepower

    def display_engine(self):
        return f"Chassis No: {self.chassis_no}, Horsepower: {self.horsepower}"


class Car:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.engine = Engine("1234", "500")

    def display_car(self):
        return f"Car Name: {self.name}, Price: {self.price}"

    def display_all_details(self):
        print("----- Car Details -----")
        print(self.display_car())
        print(self.engine.display_engine())


car_obj = Car("BMW", "1 Cr")
car_obj.display_all_details()