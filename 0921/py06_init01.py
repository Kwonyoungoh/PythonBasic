class Cls1:
    def __init__(self):
        self.__val1 = 1
        self.__val2 = 3

    def out(self):
        print(self.__val1)
        print(self.__val2)

ins1 = Cls1()
ins1.out()