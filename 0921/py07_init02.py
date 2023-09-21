class Cls1:
    def __init__(self, val1,val2):
        self._val1 =val1
        self._val2 =val2
        print('init')
        super().__init__()

    # 맨처음에 인스턴스가 실행될때 호출됨
    # init이전에
    # new매서드가 먼저 실행
    # new에서 프로퍼티 값 세팅이 불가
    # 일단 거의 안씀


    def __new__(cls, val1, val2):
        print(val1,val2)
        print('new')
        return super().__new__(cls)



ins1 = Cls1(2,4)