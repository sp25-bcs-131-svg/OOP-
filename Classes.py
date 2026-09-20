#Class

class Student():
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        print("Creating a new student")

s1 = Student("Umama",91)
print(s1.name)
print(s1.marks)

s2 = Student("Talha",82)
print(s2.name)  
print(s1.marks)
