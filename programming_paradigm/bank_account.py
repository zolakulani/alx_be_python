class BankAccount:
    """A simple bank account class that supports deposit, withdraw, and balance display operations."""
    
    def __init__(self, initial_balance=0):
        """Initialize the bank account with an optional initial balance."""
        self.account_balance = initial_balance
    
    def deposit(self, amount):
        """Deposit the specified amount into the account."""
        self.account_balance += amount
    
    def withdraw(self, amount):
        """
        Withdraw the specified amount from the account if sufficient funds are available.
        Returns True if withdrawal was successful, False otherwise.
        """
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False
    
    def display_balance(self):
        """Display the current account balance."""
        print(f"Current Balance: ${self.account_balance:.2f}")