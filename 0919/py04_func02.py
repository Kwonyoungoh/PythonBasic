from random import *


# optional prameter
# 파라미터에 입력에 대한 옵션을 주는 것이다.
def func3(n1=1, n2=2, n3=1):
    print(f'{n1} {n2} {n3}')


# 매개변수는 딕셔너리 패턴 형태로 저장됨
# 즉 key를 통한 접근이 가능하다
func3(n2=5)


# 야구게임
# 1 - 9
def ran_nums():
    lst = []
    while len(lst) < 3:
        n = randint(1, 10)
        if n in lst:
            continue
        else:
            lst.append(n)

    return lst


print(ran_nums())


def check():
    strk = 0
    ball = 0
    out = 0
    cnt = 0
    while strk < 3:
        comp_lst = ran_nums()
        usr_lst = ran_nums()

        for i in range(3):
            cnt += 1
            if usr_lst[i] in comp_lst:
                if usr_lst[i] == comp_lst[i]:
                    strk += 1
                else:
                    ball += 1
            else:
                out += 1
            break

    print(f'3 Strike {cnt} innings end')
    print(f'{strk}S {ball}B {out}O')


check()
