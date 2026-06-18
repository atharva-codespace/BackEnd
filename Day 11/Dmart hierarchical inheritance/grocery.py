from dmart import dmart

class grocery(dmart):

    def __init__(self, id, category, product_name, price, expiry, BName, manufacturing_date):

        super().__init__(id, category, product_name, price)

        self.expiry = expiry
        self.BName = BName
        self.manufacturing_date = manufacturing_date

    @classmethod
    def gdisplay(cls):

        print(f"{'Field':20}", end="")

        for i in range(2):
            print(f"Product {i+1}           ", end="")
        print()
        
        print("-" * (20 + len(items) * 20))

        print(f"{'ID':20}", end="")
        for item in items:
            print(f"{item.id:<20}", end="")
        print()

        print(f"{'Category':20}", end="")
        for item in items:
            print(f"{item.category:<20}", end="")
        print()

        print(f"{'Product':20}", end="")
        for item in items:
            print(f"{item.product_name:<20}", end="")
        print()

        print(f"{'Price':20}", end="")
        for item in items:
            print(f"{item.price:<20.2f}", end="")
        print()

        print(f"{'Brand':20}", end="")
        for item in items:
            print(f"{item.BName:<20}", end="")
        print()

        print(f"{'Mfg Date':20}", end="")
        for item in items:
            print(f"{item.manufacturing_date:<20}", end="")
        print()

        print(f"{'Expiry Date':20}", end="")
        for item in items:
            print(f"{item.expiry:<20}", end="")
        print()


g1 = grocery(1,"Dairy & Breakfast","Organic Whole Milk",44.49,"2026-06-25","DairyFresh","2026-06-15")
g2 = grocery(2,"Dairy & Breakfast","Butter",50.09,"2026-06-25","DairyFresh","2026-06-15")
items = [g1, g2]