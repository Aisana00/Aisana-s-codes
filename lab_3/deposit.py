class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount}. New balance: ${self.balance}")
        else:
                
    
    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Withdrawal denied! Insufficient funds. Balance: ${self.balance}")
        elif amount <= 0:
            print("Withdrawal amount must be positive!")
        else:
            self.balance -= amount
            print(f"Withdrew: ${amount}. New balance: ${self.balance}")
    
    def __str__(self):
        return f"Account owner: {self.owner}\nAccount balance: ${self.balance}"


# Testing the account class
if __name__ == "__main__":
    # Create an account
    account = Account("John Doe", 1000)
    
    print("=== Initial Account ===")
    print(account)
    print()
    
    # Test deposits
    print("=== Deposits ===")
    account.deposit(500)
    account.deposit(200)
    account.deposit(-50)
    print()
    
    # Test withdrawals
    print("=== Withdrawals ===")
    account.withdraw(300)
    account.withdraw(1000)
    account.withdraw(500)
    account.withdraw(0)
    print()
    
    # Final state
    print("=== Final Account State ===")
    print(account)