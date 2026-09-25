class Student():

    def __init__(self,phy,chem,bio):
        self.phy = phy
        self.chem = chem
        self.bio = bio

    @property
    def percentage(self):
        return str((self.chem+self.bio+self.phy)/3) + "%"

s1 = Student(88,91,79)
print(s1.percentage)
s1.phy = 85
print(s1.percentage)

class BankAccount():

    def __init__(self,name:str,balance:float):
        self.name = name
        # Leading underscore (_balance) signals that this attribute is internal/private
        self._balance = balance

    #getter
    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self,amount:float):
        if not isinstance(amount, (int, float)):
            raise TypeError("Balance must be a numerical value.")
        if amount < 0:
            raise ValueError("Balance cannot be negative!")

        self._balance = amount

    @balance.deleter
    def balance(self):
        del self._balance

acc = BankAccount("Talha",10000.0)
print(acc.balance)
acc.balance = 7500.0
print(acc.balance)




                