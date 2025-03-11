class BankAccount:

    def __init__(self, balance, owner_name):
        self.balance = balance
        self.owner_name = owner_name

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}, balance is now ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}, balance is now ${self.balance}")

    def get_balance(self):
        print(f"Your balance is ${self.balance}")


bankaccount1 = BankAccount(0, "Jerry")

bankaccount1.get_balance()
bankaccount1.deposit(1000)
bankaccount1.withdraw(500)
print(f"{bankaccount1.owner_name}'s final Balance: ${bankaccount1.balance}")
