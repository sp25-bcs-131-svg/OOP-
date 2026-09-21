class Account():

    def __init__(self,acc_no):
        self.__acc_no = acc_no

    def get_acc(self):
        return self.__acc_no

c1 = Account('PK4045')
#print(c1.__acc_no) causes error
print(c1.get_acc())