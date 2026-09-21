from abc import abstractmethod


class Car():

    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.acc = True
        print("car started")

c1 = Car()
c1.start()

# Abstract Class (Blueprint)
class Vehicle():

    @abstractmethod
    def start_engine(self):
        pass
