class Class1 :

    def set_data(self):
        self.aaa = 1
        self.bbb ='abc'

    def get_data(self):
        print(self.aaa)
        print(self.bbb)

    def get_total_data(self):
        print(self.aaa)
        print(self.bbb)
        self.get_data()

val1 = Class1()
val1.set_data()
val1.get_data()
val1.get_total_data()