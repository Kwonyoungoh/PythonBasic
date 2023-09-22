class Car:

    def __init__(self,a):
        self.engine = a

    def show_engine(self):
        print(self.engine)

class Lambo(Car):

    def show_engine(self):
        super().show_engine()
        print('예아~람보')

lambo1 = Lambo('람보의 엔진')
lambo1.show_engine()