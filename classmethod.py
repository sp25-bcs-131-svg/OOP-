class Person():

    name = "anonymous"

    def change_name(self,name):
        self.__class__.name = name
        #Alternative solutions
        #Person.name = name
    
    #Alternative solutions
    @classmethod
    def change_name2(cls,name):
        cls.name =name

p1 = Person()
p1.change_name2("Ahmad")
print(p1.name)
print(Person.name)
