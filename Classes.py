#Class

class Student():

    #Class Attribute
    college_name = "Comsats"

    #Default Constructors
    def __init__(self, name, bases, dict, /, **kwds):
        pass

    #Parameterized constructors
    def __init__(self,name,marks):
        #Instance Attribute
        self.name = name
        self.marks = marks

    def hello(self):
        print("hello", self.name)

    def get_marks(self):
        return self.marks
    
    

s1 = Student("Umama",91)
print(s1.name)
print(s1.get_marks())
print(s1.college_name)
s1.hello()

s2 = Student("Talha",82)
print(s2.name)  
print(s1.marks)

print(Student.college_name)
