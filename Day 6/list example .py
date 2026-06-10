x = [
    [1, "car", 500],
    [2, "doll", 1000],
    [3, "grocery", 2000],
    [4, "bottle", 5000]
]


def view():

    print("\n--------------------------------------------------")
    print("\nItems in the Bucket:\n")

    print("ID\tItem Name\tPrice")
    print("--------------------------------------------------")

    for item in x:
        print(f"{item[0]}\t{item[1]}\t\t{item[2]}")

    print("\n--------------------------------------------------\n")


ch = 0

while ch != 7:

    print("\n1.View Items")
    print("2.Add Items")
    print("3.Update Items")
    print("4.Delete Items")
    print("5.Search Item")
    print("6.Buy All Items")
    print("7.Exit\n")

    ch = int(input("Enter your choice: "))

    match ch:

        case 1:
            view()

        case 2:

            print("\n--------------------------------------------------\n")

            num = int(input("Enter how many Items you want to add: "))

            if num == 1:

                print("\nEnter Item Details:\n")

                id = int(input("Enter Item ID: "))
                name = input("Enter Item Name: ")
                price = int(input("Enter Item Price: "))

                x.append([id, name, price])

                print("\nItem Added Successfully!")

            else:

                print("\nEnter Items Details:\n")

                for i in range(num):

                    id = int(input(f"Enter Item ID {i+1}: "))
                    name = input(f"Enter Item Name {i+1}: ")
                    price = int(input(f"Enter Item Price {i+1}: "))

                    x.append([id, name, price])

                print("\nItems Added Successfully!")

            view()


        case 3:

            view()

            num = int(input("Enter how many Items you want to update: "))

            for k in range(num):

                pid = int(input(f"\nEnter ID of {k+1} Item to update: "))

                found = False

                for item in x:

                    if item[0] == pid:

                        found = True

                        print("\n1. Item ID")
                        print("2. Item Name")
                        print("3. Item Price")
                        print("4. Update All\n")

                        choice = int(input("Enter what you want to update: "))

                        match choice:

                            case 1:

                                newid = int(input("Enter new Item ID: "))
                                item[0] = newid

                            case 2:

                                newname = input("Enter new Item Name: ")
                                item[1] = newname

                            case 3:

                                newprice = int(input("Enter new Item Price: "))
                                item[2] = newprice

                            case 4:

                                newid = int(input("Enter new Item ID: "))
                                newname = input("Enter new Item Name: ")
                                newprice = int(input("Enter new Item Price: "))

                                item[0] = newid
                                item[1] = newname
                                item[2] = newprice

                            case _:

                                print("Invalid Choice!")

                        print("\nItem Updated Successfully!")

                        view()

                        break

                if found == False:
                    print("Item Not Found!")


        case 4:

            view()

            num = int(input("Enter how many Items you want to delete: "))

            for k in range(num):

                pid = int(input(f"Enter Item ID {k+1} to delete: "))

                found = False

                for i in range(len(x)):

                    if x[i][0] == pid:

                        x.pop(i)

                        found = True

                        print("Item Deleted Successfully!")

                        break

                if found == False:
                    print("Item Not Found!")

            view()


        case 5:

            view()

            num = int(input("Enter how many Items you want to search: "))

            for i in range(num):

                id = int(input(f"Enter Item ID {i+1} to search: "))

                found = False

                for j in range(len(x)):

                    if x[j][0] == id:

                        print("\nID\tItem Name\tPrice")
                        print("--------------------------------")

                        print(f"{x[j][0]}\t{x[j][1]}\t\t{x[j][2]}")

                        found = True

                        break

                if found == False:
                    print(f"Item with ID {id} not available")


        case 6:

            print("\n---------------- BILL ----------------\n")

            total_price = 0
            total_gst = 0

            print("ID\tItem Name\tPrice\tGST\tTotal")
            print("--------------------------------------------------")

            for item in x:

                price = item[2]

                # GST Calculation

                if price <= 500:

                    gst = price * 0.05

                elif price <= 1000:

                    gst = (500 * 0.05) + ((price - 500) * 0.12)

                elif price <= 2000:

                    gst = (500 * 0.05) + (500 * 0.12) + ((price - 1000) * 0.18)

                else:

                    gst = (500 * 0.05) + (500 * 0.12) + (1000 * 0.18) + ((price - 2000) * 0.28)

                final_price = price + gst

                total_price += price
                total_gst += gst

                print(f"{item[0]}\t{item[1]}\t\t{price}\t{gst:.2f}\t{final_price:.2f}")

            grand_total = total_price + total_gst

            print("\n--------------------------------------------------")

            print(f"Total Price : {total_price}")
            print(f"Total GST   : {total_gst:.2f}")
            print(f"Final Amount: {grand_total:.2f}")

            print("\n--------------------------------------------------")


        case 7:

            print("\nExiting Program...\n")


        case _:

            print("\nInvalid Choice! Please Try Again.\n")