class Student():

    def __init__(self,name,marks1,marks2,marks3):
        self.name = name
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3

    #Non static method  
    def average(self):
        avg = (self.marks1+self.marks2+self.marks3) / 3
        return avg

    @staticmethod
    def college():
        print("Comsats University")


s1 = Student("Talha",81,88,76)
print(s1.average())
Student.college()
    