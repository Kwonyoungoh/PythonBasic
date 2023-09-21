class Scv:

    def __init__(self):
        self.hp = 50
        self.atk = 5
        self.dfns = 2

    def attack(self):
        print(f'{self.atk}의 공격을 가함')

    def defence(self):
        print(f'{self.dfns}만큼을 방어')
        self.hp -= self.atk - self.dfns

    def get_hp(self):
        print(f'hp : {self.hp}')

scv1 ={'atk':3,'hp':50,'dfns' :2}

def atk1(dic1):
    atk = dic1['atk']
    print(f'{atk}의 공격을 가함')

def dfns1(dic1):
    dfns = dic1['dfns']
    print(f'{dfns}의 공격을 방어')
    dic1['hp'] -= dic1['atk'] - dfns

atk1(scv1)
dfns1(scv1)
print(scv1)

scv02 = Scv()

scv02.attack()
scv02.defence()
scv02.get_hp()