class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        self.__balance = amount

    def __deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"\n₹{amount} deposited successfully.")
            print(f"Current Balance : ₹{self.__balance}")
        else:
            print("\nInvalid deposit amount.")

    def __withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"\n₹{amount} withdrawn successfully.")
            print(f"Remaining Balance : ₹{self.__balance}")
        else:
            print("\nInsufficient Balance.")

    def deposit_money(self, amount):
        self.__deposit(amount)

    def withdraw_money(self, amount):
        self.__withdraw(amount)


initial_balance = float(input("Enter Initial Balance: ₹"))
account = BankAccount(initial_balance)
choice=0
while choice!=4:

    print("\n========== BANK MENU ==========")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    print("===============================")

    choice = int(input("Enter Your Choice: "))

    match choice:

        case 1:
            print(f"\nCurrent Balance : ₹{account.get_balance()}")

        case 2:
            amount = float(input("Enter Deposit Amount: ₹"))
            account.deposit_money(amount)

        case 3:
            amount = float(input("Enter Withdrawal Amount: ₹"))
            account.withdraw_money(amount)

        case 4:
            print("\nThank you for using our banking system!")
            break

        case _:
            print("\nInvalid Choice! Please try again.")