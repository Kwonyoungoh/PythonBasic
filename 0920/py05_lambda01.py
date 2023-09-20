hello = lambda: print('hello lambda')

hello()

print((lambda a, b: a - b)(7, 5))


def func2(a):
    print(a)


func2((lambda a: f'{a}')('hello lambda'))


# 람다식은 함수째로 리턴도 가능하다.
def func3():
    return lambda x: x ** 2


x1 = func3()
print(x1(3))

def func4():
    print('복잡한 수식')
    return 1

x3 = lambda x : x+func4()

print(x3(3))