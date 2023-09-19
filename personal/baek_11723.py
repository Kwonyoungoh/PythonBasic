import sys
class Set:

    def __init__(self):
        # 공집합 만들 시 set()쓰셈
        self.set1 = set()

    def _add(self, n):
        self.set1.add(n)

    def _remove(self, n):
        # discard는 해당 값이 없어도 에러 발생 X
        self.set1.discard(n)

    def _check(self, n):
        if n in self.set1:
            print(1)

        else:
            print(0)

    def _toggle(self, n):
        if n in self.set1:
            self.set1.discard(n)
        else:
            self.set1.add(n)

    def _all(self):
        self.set1 = {a for a in range(1, 21)}

    def _empty(self):
        self.set1 = set()


cnt = int(sys.stdin.readline().rstrip())
s1 = Set()
for _ in range(cnt):
    ord = sys.stdin.readline().rstrip()
    ord_lst = ord.split(' ')

    # order
    if ord_lst[0] in ['add','remove','toggle','check']:
        n = int(ord_lst[1])
    else:
        if ord_lst[0] == 'all':
            s1._all()
        elif ord_lst[0] == 'empty':
            s1._empty()
        continue

    if ord_lst[0] == 'add':
        s1._add(n)
    elif ord_lst[0] == 'remove':
        s1._remove(n)
    elif ord_lst[0] == 'check':
        s1._check(n)
    elif ord_lst[0] == 'toggle':
        s1._toggle(n)