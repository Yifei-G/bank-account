class Bank_Account_Exception(Exception):

    def __init__(self, message):
        Exception.__init__(self, message)
        self.error_message = message

    def account_number_error(self):
        return self.error_message

    def account_balance_error(self):
        return self.error_message

    def delete_account_number_error(self):
        return self.error_message
