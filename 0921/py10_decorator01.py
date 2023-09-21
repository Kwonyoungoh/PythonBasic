def deco_func(origin_func):
    def wrap_func(*args, **kwargs):
        print('before ', origin_func.__name__)
        return origin_func(*args, **kwargs)

    return wrap_func

# lambda로 해볼까?
def deco_func2(origin_func):
    return lambda *args, **kwargs: (print('before ', origin_func.__name__), origin_func(*args, **kwargs))[1]

@deco_func
def dis_1():
    print('dis_1()')


@deco_func
def dis_2():
    print('dis_2()')


@deco_func2
def dis_3(n, a):
    print(f'after {n} {a}')


dis_1()
dis_2()
# 샐행 할 경우 받은 파라미터가 deco_func에서는 없기 때문에 에러가 난다.
dis_3(1,2)
