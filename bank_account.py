from bank_account_exception import Bank_Account_Exception as error


class Bank_Account:

    def __init__(self, account_number):
        self.__account_number = account_number
        self.__account_balance = 0

    @property
    def account_number(self):
        return self.__account_number

    @account_number.setter
    def account_number(self, account_number):
        raise error("You can't modify the account number!")

    @account_number.deleter
    def account_number(self):
        if self.__account_balance != 0:
            raise error(
                "You can't delete the account becase you still have money in your account!")
        else:
            self.__account_number = None
            self.__account_balance = None
            print("Account has been sucessfully deleted!")

    @property
    def account_balance(self):
        return self.__account_balance

    @account_balance.setter
    def account_balance(self, value):
        if (value < 0) and ((type(value) != float) or (type(value) != int)):
            raise error("The balance for your account is not a valid value!")
        if abs(self.__account_balance - value) > 100_000:
            print(
                "You are operating more than 100000, this operation will be registered!")
        self.__account_balance = value
