class BankAccount:
    def __init__(self, balance):
        self.__balcance = balance
        self.__interest_rate = 0.05
    def get_balance(self):
        return self.__balcance
    def get_interest_rate(self, rate):
        return self.__interest_rate



# Method Overriding
class Dog:
    def speak(self):
        return "Woof! Woof!"

class cat:
    def speak(self):
        return "Meow!"
    
x = [Dog(), cat()]
for i in x:
    print(i.speak())


# Method Overloading
class calculator:
    def add(self, *args):
        return sum(args)
    
calc = calculator()
print(calc.add(1, 2))  # Output: 3
print(calc.add(1, 2, 3))  # Output: 6
print(calc.add(1, 2, 3, 4))  # Output: 10