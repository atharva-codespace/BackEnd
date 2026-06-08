unit = int(input("Enter electricity units consumed: "))

if unit <= 100:
    total = unit * 2

elif unit <= 200:
    total = (100 * 2) + ((unit - 100) * 3)

else:
    total = (100 * 2) + (100 * 3) + ((unit - 200) * 5)

print("\n----- ELECTRICITY BILL -----")
print(f"Units Consumed : {unit}")
print(f"Total Bill     : ₹{total}")

