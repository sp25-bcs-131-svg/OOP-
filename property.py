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
        