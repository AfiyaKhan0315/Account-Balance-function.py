def CashDeposit(UserBalance, UserAmount):
    Balance = UserBalance
    Amount = UserAmount
    NewBalance = Balance + Amount
    TransactionID = "HBL123"

    print("WELCOME TO HBL BANK")
    print(f"Your amount {Amount} is deposited successfully")
    print(f"Your new balance is: {NewBalance}")
    print(f"Your transaction ID is: {TransactionID}, Balance{NewBalance}aff12{Amount}")

CashDeposit(9000, 7000)