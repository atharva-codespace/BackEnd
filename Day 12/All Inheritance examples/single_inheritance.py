class Appliance:
    def __init__(self, brand, power):
        self.brand = brand
        self.power = power

    def turn_on(self):
        return f"{self.brand} appliance is now turned on."

    def display_appliance_info(self):
        print(f"Brand : {self.brand}")
        print(f"Power : {self.power} W")


class WashingMachine(Appliance):
    def __init__(self, brand, power, capacity, wash_mode):
        super().__init__(brand, power)
        self.capacity = capacity
        self.wash_mode = wash_mode

    def start_wash(self):
        return f"{self.brand} washing machine has started in {self.wash_mode} mode."

    def display_washing_machine_info(self):
        self.display_appliance_info()
        print(f"Capacity  : {self.capacity} kg")
        print(f"Wash Mode : {self.wash_mode}")


def run_demo():
    wm = WashingMachine(brand="LG",power=1500,capacity=7,wash_mode="Quick Wash")

    print("Output:")
    print(wm.turn_on())
    wm.display_washing_machine_info()
    print(wm.start_wash())