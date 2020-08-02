from bank_account import Bank_Account
from bank_account_exception import Bank_Account_Exception


account1 = Bank_Account("ES51775049303")

print("The account number is:", account1.account_number)
try:
    print("Trying to set the account number to: ES51775049305")
    account1.account_number = "ES51775049305"
except Bank_Account_Exception as error:
    print(error.account_number_error())

print("The account number is:", account1.account_number)

account1.account_balance += 1200.5
print("The account balance is:", account1.account_balance)

account1.account_balance += 1000_000
print("The account balance is:", account1.account_balance)


try:
    print("Trying to set account blance to: -1000000")
    account1.account_balance = -1000000
except Bank_Account_Exception as error:
    print(error.account_balance_error())


try:
    print("Trying to delete the account number")
    del account1.account_number
except Bank_Account_Exception as error:
    print(error.delete_account_number_error())
