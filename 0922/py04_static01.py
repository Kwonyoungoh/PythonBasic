class Cls:
    n = 'name'

    def __init(self,aaa):
        self.aaa = aaa

    @staticmethod
    def add(x,y):
        return x+ y


    # 얘는 클래스 맴버에 대한 접근이 허용된다.
    # __new__ 처럼 클래스 접근이 가능함
    @classmethod
    def class_info(cls):
        print(cls.n)


print(Cls.add(1,2))
Cls.class_info()