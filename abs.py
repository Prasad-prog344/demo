class BankAccount:
    __accountNumber = None
    __accountHolder = None
    __balance = None

    def __init__(self, accountNumber, accountHolder):
        BankAccount.__accountNumber = accountNumber
        BankAccount.__accountHolder = accountHolder
        BankAccount.__balance = 0

    def deposit(self, value):
        BankAccount.__balance += value
        print(f"Deposited: ${value}")

    def withdraw(self, value):
        BankAccount.__balance -= value
        print(f"Withdrawn: ${value}")

    def getAccountInfo(self):
        print(f"Account Number: {BankAccount.__accountNumber}")
        print(f"Account Holder: {BankAccount.__accountHolder}")
        print(f"Balance: ${BankAccount.__balance}")

    # Create a BankAccount object


account = BankAccount(12345, "John Doe")

# Perform deposits and withdrawals and display account info
account.deposit(1000)
account.withdraw(500)
account.deposit(200)

# Display the final account information
account.getAccountInfo()
rows = int(input("Enter the number of rows: "))
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))


