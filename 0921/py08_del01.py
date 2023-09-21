class Cls1:
    def __init__(self,name):
        self.name = name

    def print_info(self):
        print(f'name : {self.name}')

    # 소멸자
    def __del__(self):
        print(f'bye {self.name}')

usr1 = Cls1('JUNE')
usr1.print_info()
usr2 = Cls1('JULLIE')
usr2.print_info()

# 사용했던 인스턴스 삭제시!
del usr2
del usr1