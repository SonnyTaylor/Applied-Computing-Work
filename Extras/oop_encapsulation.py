class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  # Private attribute
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance!")

    def get_balance(self):
        return self.__balance


# Example usage
account = BankAccount("123456", 100)
print(account.get_balance())  # 100
account.deposit(50)
print(account.get_balance())  # 150
account.withdraw(30)
print(account.get_balance())  # 120
account.withdraw(200)  # Insufficient balance lol
print(account.get_balance())  # 120
