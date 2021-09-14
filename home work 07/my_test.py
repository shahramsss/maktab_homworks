class Account:
    min_remaining = 0

    def __init__(self, name, remaining):
        self.name = name
        self.remaining = remaining
        self.min_remaining = remaining

    def deposit(self, number_deposit):
        self.min_remaining = self.min_remaining + number_deposit

    def withdraw(self, number_withdraw):
        if self.__test_number_account(number_withdraw):
            self.min_remaining = self.min_remaining - number_withdraw

    def transport(self, destination_account, number_transfer):
        if self.__test_number_account(number_transfer):
            self.min_remaining = self.min_remaining - number_transfer
            destination_account = destination_account + number_transfer

    def __test_number_account(self, number_test):
        if self.min_remaining - number_test > 0:
            print("This operation is not executable")
            return False
        else:
            return True
