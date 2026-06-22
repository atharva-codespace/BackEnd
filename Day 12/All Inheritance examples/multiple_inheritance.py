class Camera:
    def __init__(self, megapixels):
        self.megapixels = megapixels

    def click_photo(self):
        return f"Photo clicked at {self.megapixels}MP resolution."


class Phone:
    def __init__(self, network):
        self.network = network

    def make_call(self, number):
        return f"Calling {number} over the {self.network} network..."


class Smartphone(Camera, Phone):
    def __init__(self, brand, megapixels, network):
        Camera.__init__(self, megapixels)
        Phone.__init__(self, network)
        self.brand = brand

    def install_app(self, app_name):
        return f"'{app_name}' has been installed on the {self.brand} smartphone."

    def display_smartphone_info(self):
        print(f"Brand      : {self.brand}")
        print(f"Camera     : {self.megapixels}MP")
        print(f"Network    : {self.network}")


def run_demo():
    phone = Smartphone(brand="Samsung", megapixels=108, network="5G")

    print("Output:")
    phone.display_smartphone_info()
    print(phone.click_photo())            
    print(phone.make_call("9876543210"))  
    print(phone.install_app("WhatsApp"))  
