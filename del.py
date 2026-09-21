class People():

    def __init__(self,name):
        self.name = name

    def get_name(self):
        return self.name

    def set_name(self,new_name):
        self.name = new_name

p1 = People("Talha")
print(p1.get_name())
p1.set_name("Ahmad")
print(p1.get_name())

del p1.name
del p1

        