class Account():

    def __init__(self,acc_no):
        self.__acc_no = acc_no

    def get_acc(self):
        return self.__acc_no

c1 = Account('PK4045')
#print(c1.__acc_no) causes error
print(c1.get_acc())

class Person():

    __name = "Talha" # Private Attribute

    def __hello(self): # Private Method
        print("hello,",self.__name)

    def welcome(self):
        self.__hello()

p1 = Person()
#p1.__hello()
print(p1.welcome())
