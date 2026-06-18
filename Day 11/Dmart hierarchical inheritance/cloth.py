from dmart import dmart

class clothes(dmart):
    def __init__(self, id, category, product_name, price, color, size):
        super().__init__(id, category, product_name, price)
        self.color = color
        self.size = size
    @classmethod
    def cdisplay(cls):
        print(f"{'Field':20}", end="")

        for i in range(2):
            print(f"Product {i+1}           ", end="")
        print()

        print("-" * (50))
        print(f"{'id':20}",end="")
        for item in cloth_items:
            print(f"{item.id:<20}",end="")
        print()

        print(f"{'Category':20}", end="")
        for item in cloth_items:
            print(f"{item.category:20}", end="")
        print()

        print(f"{'Product':20}", end="")
        for item in cloth_items:
            print(f"{item.product_name:20}", end="")
        print()

        print(f"{'Price':20}", end="")
        for item in cloth_items:
            print(f"{item.price:<20}", end="")
        print()

        print(f"{'Color':20}", end="")
        for item in cloth_items:
            print(f"{item.color:20}", end="")
        print()

        print(f"{'Size':20}", end="")
        for item in cloth_items:
            print(f"{item.size:20}", end="")
        print()


        
c1 = clothes(1,"Apparel", "Slim Fit Jeans", 39.99,"Dark Denim", "32x32")
c2 = clothes(2,"Apparel", "Tshirt", 39.99,"Dark Denim", "32x32")
cloth_items=[c1,c2]
