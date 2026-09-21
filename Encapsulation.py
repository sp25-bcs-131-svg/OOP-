class Student():

    def __init__(self,name,marks):
        self.name = name
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def set_marks(self,new_marks):
        if 0 <= new_marks <= 100:
            self.__marks = new_marks
            print("Marks updated successfully!")
        else:
            print("Invalid marks! Value must be between 0 and 100.")

s1 = Student("Talha",85)
print(s1.get_marks())
s1.set_marks(91)
print(s1.get_marks())
