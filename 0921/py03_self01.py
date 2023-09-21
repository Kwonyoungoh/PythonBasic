class Cls1:
    def get_self(self):
        print(self)
        print(id(self))

inst1 = Cls1()
inst1.get_self()
print(id(inst1))