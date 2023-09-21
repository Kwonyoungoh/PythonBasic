class Cls1:
    s = 1
    def set_data1(self,val1,val2,val3):
        self._val1 =val1
        # 비공개 속성
        self.__val2 = val2
        # 예외 사항
        # 양쪽에 __붙으면 공용으로 사용하는 레퍼런스라고 생각됨
        self.__val3__ = val3

    def __func1(self):
        print('i am 비공개')

ins1 = Cls1()
ins1.set_data1(10,15,20)
# _하나는 경고
print(ins1._val1)
# __ 두개는 메소드를 통해서만 접근가능
# print(ins1.__val2)
print(ins1.__val3__)