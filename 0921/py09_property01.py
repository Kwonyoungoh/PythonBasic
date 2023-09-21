class Person:

    bag = []
    val1 = 123

    def __init__(self,val2):
        self.bag2 = []
        self.val2 =val2

    def put_bag1(self, stuff):
        self.bag.append(stuff)

    def put_bag2(self,stuff):
        self.bag2.append(stuff)

    def minus_val(self,n):
        # 하지만 값에의해 변경이된다.
        self.val1-=n

    # annotation 쓰면됨
    @staticmethod
    # 이건 클래스 메소드
    def cla_method():
        print('cls method')

# 클래스 메소드
# 퍼블릭 메소드 생각하면 된다.
Person.cla_method()

per1 = Person(456)
per1.put_bag1('book')# 클래스 필드에 삽입
per1.put_bag2('book')# 인스턴스 필드에 삽입

per2 = Person(789)
per2.put_bag1('key')
per2.put_bag2('key')

# 클래스끼리 공유 상수로 사용이 가능하다.
print(per1.bag)
print(per1.bag2)
print(per2.bag)
print(per2.bag2)

per1.minus_val(10)
per2.minus_val(10)

print(per1.val1)
print(per2.val1)