class BankAccount:
    def __init__(self, accnum,holdername,
  balance=0.0):
        self.__accnum = accnum
        self.__holdername = holdername
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount} into {self.__holdername}'s account.")
        else:
            print("Invalid deposit amount. Amount must be greater than 0.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount} from {self.__holdername}'s account.")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def display_balance(self):
        print(f"Account Number: {self.__accnum}")
        print(f"Account Holder: {self.__holdername}")
        print(f"Account Balance: ${self.__balance:.2f}")
if __name__ == "__main__":
    
    account = BankAccount("123456789", "John Doe", 1000.0)

    
    account.display_balance()

    
    account.deposit(500)

    
    account.display_balance()

    
    account.withdraw(200)

    
    account.display_balance()

    
    account.withdraw(1500)
