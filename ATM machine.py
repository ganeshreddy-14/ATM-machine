class Bank:
    pin = 1234
    pincount = 1
    acbal_saving = 10000
    acbal_current = 50000
    wcount_saving = 0
    wcount_current = 0
    account_type = None

    def selectAccount(self):
        print("Select Account Type:")
        print("1. Savings Account")
        print("2. Current Account")
        acc = int(input("Enter your choice: "))
        if acc == 1:
            self.account_type = "saving"
            obj.viewOptions()
        elif acc == 2:
            self.account_type = "current"
            obj.viewOptions()
        else:
            print("Invalid choice, please try again")
            obj.selectAccount()

    def viewOptions(self):
        print("1. Deposit ")
        print("2. Withdraw ")
        print("3. Balance Enquiry ")
        print("0. EXIT ")
        opt = int(input("Choose your option: "))
        if opt == 1:
            obj.deposit()
            obj.confirm()
        elif opt == 2:
            if (self.account_type == "saving" and self.wcount_saving < 3) or (self.account_type == "current" and self.wcount_current < 5):
                obj.withdraw()
                obj.confirm()
            else:
                print("Withdraw limit is over, please try after 24 hrs")
        elif opt == 3:
            if self.account_type == "saving":
                print("Available balance (Savings): ", self.acbal_saving)
            else:
                print("Available balance (Current): ", self.acbal_current)
            obj.confirm()
        elif opt == 0:
            print("Thank you, Visit again")
        else:
            print("Invalid option, please try again")
            obj.viewOptions()

    def validate(self):
        pin = int(input("Enter your pin: "))
        if self.pin == pin:
            obj.selectAccount()
        else:
            self.pincount += 1
            if self.pincount <= 3:
                print("Invalid pin, please try again")
                obj.validate()
            else:
                print("Your card is blocked for the day")

    def deposit(self):
        amt = int(input("Enter deposit amount: "))
        if amt % 100 == 0:
            if amt <= 50000:
                if self.account_type == "saving":
                    self.acbal_saving += amt
                    print("Available balance (Savings): ", self.acbal_saving)
                else:
                    self.acbal_current += amt
                    print("Available balance (Current): ", self.acbal_current)
            else:
                print("Transaction limit is 50000 only")
        else:
            print("Please enter multiples of 100")

    def confirm(self):
        opt = int(input("1.Continue \n0.EXIT "))
        if opt == 1:
            obj.viewOptions()
        else:
            print("Thank you, Visit again")

    def withdraw(self):
        amt = int(input("Enter withdraw amount: "))
        if amt % 100 == 0:
            if self.account_type == "saving":
                if amt <= self.acbal_saving:
                    if amt <= 20000:
                        self.acbal_saving -= amt
                        self.wcount_saving += 1
                        print("Available balance (Savings): ", self.acbal_saving)
                    else:
                        print("Transaction limit is 20000 only")
                else:
                    print("Insufficient fund")
            else:
                if amt <= self.acbal_current:
                    if amt <= 50000:
                        self.acbal_current -= amt
                        self.wcount_current += 1
                        print("Available balance (Current): ", self.acbal_current)
                    else:
                        print("Transaction limit is 50000 only")
                else:
                    print("Insufficient fund")
        else:
            print("Please enter multiples of 100 only")


obj = Bank()
obj.validate()
