from abc import *

class ParentsD(metaclass=ABCMeta):
    def get_handle(self):
        print('손잡이')

    @abstractmethod
    def get_point(self):
        pass

class ChildD(ParentsD):
    def get_point(self):
        print('cross d')


testD = ChildD()

testD.get_point()