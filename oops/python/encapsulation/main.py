# Getter and Setter Method


class Banking:
    def __init__(self,account_holder,balance=0):
        self.account_holder = account_holder
        self.__balance = balance
    def get_balance(self):
        return self.__balance
    def set_balance(self,amount):
        self.__balance += amount
        return f"Your balance was set successfully"
    