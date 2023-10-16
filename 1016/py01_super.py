class super_c:
    # 생성자
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def s_mth(self):
        print('im super')


class sub_c(super_c):
    def __init__(self, name, country):
        super().__init__(name, country)

    def s_mth(self):
        # 재귀 참조를 방지하기 위해 그냥 super() 키워드를 사용한다.
        super().s_mth()
        print('sub method')


obj1 = sub_c('tom', 'boy')
obj1.s_mth()
