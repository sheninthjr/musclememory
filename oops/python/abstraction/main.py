from abc import ABC, abstractmethod

class Banking(ABC):
    def __init__(self,account_holder,balance=0):
        self.account_holder = account_holder
        self._balance = balance
    
    @abstractmethod
    def deposit(self,amount):
        pass

    @abstractmethod
    def withdraw(self,amount):
        pass

class Savings(Banking):
    def __init__(self, account_holder, balance=0):
        super().__init__(account_holder, balance)
    def deposit(self, amount):
        self._balance += amount
        return f"Your balance is {self._balance}"
    
