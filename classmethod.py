class Person():

    name = "anonymous"

    def change_name(self,name):
        self.name = name

p1 = Person()
p1.change_name("Ahmad")
print(p1.name)
print(Person.name)
