class Cls1:
    def set_data1(self,val1,val2):
        self.val1 = val1
        self.val2 = val2

    def get_data1(self):
        print(self.val1)
        print(self.val2)

ins1 = Cls1()
ins1.set_data1(1,2)
ins1.get_data1()

print(f'-'*40)

class Cls2:

    def set_data1(self,val1,val2):
        self.val1 = val1
        self.val2 = val2

ins2 = Cls2()
ins2.set_data1(2,3)
# 파이썬은 접근제어자 없이 어떻게 접근을 제어하나?
