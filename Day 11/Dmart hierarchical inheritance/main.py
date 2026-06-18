from grocery import grocery, items, g1, g2
from cloth import clothes, c1, c2, cloth_items
cart = []

while True:

    print("\n========== DMART ==========")
    print("1. View Grocery")
    print("2. View Clothing")
    print("3. Add Grocery To Cart")
    print("4. Add Clothing To Cart")
    print("5. Generate Bill")
    print("6. Exit")

    ch = int(input("Enter Choice : "))

    match ch:

        case 1:
            grocery.gdisplay()

        case 2:
            clothes.cdisplay()
           

        case 3:

            pid = int(input("Enter Product ID : "))
            qty = int(input("Enter Quantity : "))

            found = False

            for item in items:

                if item.id == pid:

                    cart.append({
                        "name": item.product_name,
                        "price": item.price,
                        "qty": qty
                    })

                    found = True
                    print("Grocery Added Successfully!")
                    break

            if found == False:
                print("Invalid Product ID")

        case 4:

            pid = int(input("Enter Product ID : "))
            qty = int(input("Enter Quantity : "))

            cloth_items = [c1, c2]

            found = False

            for item in cloth_items:

                if item.id == pid:

                    cart.append({
                        "name": item.product_name,
                        "price": item.price,
                        "qty": qty
                    })

                    found = True
                    print("Clothing Added Successfully!")
                    break

            if not found:
                print("Invalid Product ID")

        case 5:

            if len(cart) == 0:
                print("Cart is Empty!")
                continue

            print("\n") 
            print("=" * 80) 
            print(f"{"DMART BILL":>40}") 
            print("=" * 80) 
            print(f"{'Item':35}{'Price':24}{'Qty':15}{'Amount':15}") 
            print("-" * 80) 
            grand_total = 0 
            for item in cart: 
                amount = item["price"] * item["qty"] 
                grand_total += amount 
                print( f"{item['name']:20}" f"{item['price']:20}" f"{item['qty']:20}" f"{amount:20.2f}" ) 
                print("-" * 80) 
            print(f"{'Grand Total':73} : {grand_total:.2f}") 
            print("=" * 80)
            cart=[]

        case 6:
            print("Thank You For Shopping!")
            break

        case _:
            print("Invalid Choice")