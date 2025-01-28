

class Bank:
    def __init__(self,account_holder,balance=0):
        self.account_holder = account_holder
        self.__balance = balance
    def deposit(self,amount):
        self.__balance += amount
        return f"Your current balance is {self.__balance}"
    def withdraw(self,amount):
        if self.__balance < amount:
            return f"Insufficient balance, Available balance is {self.__balance}"
        self.__balance -= amount
        return f"With draw amount is {amount} and the current balance is {self.__balance}"
    
class SavingsAcccout(Bank):
    def __init__(self,account_holder,balance=0,interest_rate=0.2):
        super().__init__(account_holder,balance)
        self.interest_rate = interest_rate
    def add_interest(self):
        self._Bank__balance += self.interest_rate * self._Bank__balance
        return f"New balance is {self._Bank__balance}"

savings = SavingsAcccout("Sheninth", 100)
print(savings.deposit(10))
print(savings.add_interest())



# class Bank:
#     def __init__(self,account_holder,balance=0):
#         self.account_holder = account_holder
#         self.balance = balance
#     def deposit(self,amount):
#         self.balance += amount
#         return f"Your current balance is {self.balance}"
#     def withdraw(self,amount):
#         if self.balance < amount:
#             return f"Insufficient balance, Available balance is {self.balance}"
#         self.balance -= amount
#         return f"With draw amount is {amount} and the current balance is {self.balance}"
    
# class SavingsAcccout(Bank):
#     def __init__(self,account_holder,balance=0,interest_rate=0.2):
#         super().__init__(account_holder,balance)
#         self.interest_rate = interest_rate
#     def add_interest(self):
#         self.balance += self.interest_rate * self.balance
#         return f"New balance is {self.balance}"

# savings = SavingsAcccout("Sheninth", 100)
# print(savings.deposit(10))
# print(savings.add_interest())

# class Animal:
#     def __init__(self,name):
#         self.name = name
#     def speak(self):
#         return f"{self.name} makes a sound"
    
# class Dog(Animal):
#     def speak(self):
#         return f"{self.name} says Woof!"
    
# dog = Dog("Tommy")
# print(dog.speak())