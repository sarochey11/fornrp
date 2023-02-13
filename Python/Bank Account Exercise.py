# Define the accounts dictionary as a global variable
accounts = {
  123456: ("John Doe", 1000),
  654321: ("Jane Doe", 10000)
}

class BankAccount:
    def __init__(self, account_ref):
        global accounts

        self.name, self.balance = accounts[account_ref]

    def check_balance(self):
        print(f"\nYour current balance is: £{self.balance}")
        return self.balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            # Don't allow the withdrawal if it would cause the balance to go negative
            print("\nInsufficient funds")
            return self.balance
        else:
            # Subtract the given amount from the balance
            self.balance -= amount
            print("\nWithdrawal successful")
            return self.balance

    def deposit(self, amount):
        if amount < 0:
            print("\nInvalid amount")
            return self.balance
        else:
            self.balance += amount
            print("\nDeposit successful")
            return self.balance
    
    def transfer(self, other_account, amount, account_ref):
        self.balance -= amount

        for i in accounts:

            if other_account == i:

                while amount >= 0 or amount <= self.balance:
                    transferAccount = accounts[i][1]
                    transferAccount += amount
                    print("\nTransfer successful")
                    return self.balance

def main():
    try:
        account_ref = int(input("\nPlease enter your reference number: "))
        for i in accounts:
            userAccount = BankAccount(i)

            if account_ref == i:
                
                accountOpen = True
                name, balence = accounts[account_ref]
                print(f"\nWelcome {name}!")
                print(i)
                while accountOpen == True:

                    print("\nPlease select an option:")
                    print("1. Check balance")
                    print("2. Withdraw")
                    print("3. Deposit")
                    print("4. Transfer")
                    print("5. Quit")
                    option = int(input("\nOption: "))

                    if option == 1:
                        userAccount.check_balance()
                    elif option == 2:
                        amount = int(input("Amount withdrawn: "))
                        userAccount.withdraw(amount)
                        print
                        userAccount.check_balance()
                    elif option == 3:
                        amount = int(input("Amount deposited: "))
                        userAccount.deposit(amount)
                        userAccount.check_balance()
                    elif option == 4:
                        other_account = int(input("Other account: "))
                        amount = int(input("Amount: "))
                        userAccount.transfer(other_account, amount, account_ref)
                        userAccount.check_balance()
                    elif option == 5:
                        accountOpen = False
                        print("\nThank you for using our service!")
                        print(f"Returned to main menu")
                        main()
                    else:
                        print("Invalid option")
                else:
                    print("Your account does not exist")
                    break
        else:
            print("Your account does not exist")
            main()
            
    except ValueError:
        print("Invalid input")
        main()
                


print("Welcome to the bank")
main()
