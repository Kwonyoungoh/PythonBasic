# 다중상속

class Person:
    def __init__(self,name):
        self.name = name
    def greating(self):
        print('hi')

class Univ:

    def __init__(self,uname):
        self.uname = uname
    def m_crdit(self):
        print('manage credit')


# 다중상속은 안쓰는게 좋다.
# 생성자 접근이 애매하다.
# 전혀 권장하지 않는다.
# 연쇄상속형태로 사용하자!!!
class UnderGrad(Person,Univ):
    def __init__(self,name,uname):
        super().__init__(name)
    def study(self):
        print('study')


tom = UnderGrad('tom','MIT')

print(tom.name)
print(tom.uname)
