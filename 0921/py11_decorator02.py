# 웹서버 구현 시 토큰 체킹같은거 할때 쓴다.
class DecoClass:
    def __init__(self, origin_func):
        self.origin_func = origin_func

    # 콜백함수 생각하셈
    def __call__(self, *args, **kwargs):
        print(f'before {self.origin_func.__name__}()')
        val = self.origin_func(*args, **kwargs)
        print(f'after deco {self.origin_func.__name__}')
        return val if bool(val) else None


@DecoClass
def dis1():
    print('after dis1()')


@DecoClass
def dis2(a, b):
    print(f'after dis2() {a} {b}')


dis1()
dis2(11, 12)
