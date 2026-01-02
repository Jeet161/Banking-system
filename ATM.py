class atm:
    def __init__(self,pin,balance):
        self.pin= pin
        self.balance= balance
    def check(self):
        n=int(input("enter PIN  :"))
        if n== self.pin:
            return True
        else:
            print("PIN invalid")
            return False
    def check_balance(self):
        print("Your balance is:", self.balance)
        
    def withdraw(self):
        amount= int(input("enter amount:"))
        if amount <= self.balance:
            self.balance -= amount
            print("withdrawal successful")
            print("Updated balance:", self.balance)
        else:
            print("no enough balance")
    def deposit(self):
        amount = int(input("enter amount:"))
        self.balance += amount
        print("deposit successful")
        print("Updated balance:", self.balance)
    
#main code
ATM= atm(pin=12345,balance=10000)

if ATM.check():
    while True:
        print("\n1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Exit")
    
        choice=int(input("enter choice:"))
        if choice == 1:
            ATM.check_balance()
        elif choice == 2:
            ATM.withdraw()
        elif choice == 3:
            ATM.deposit()

        elif choice == 4:
            print("Thank you for using the ATM")
            break
        else:
            print("Invalid choice")
            