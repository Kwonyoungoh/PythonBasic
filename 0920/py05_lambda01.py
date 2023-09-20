hello = lambda : print('hello lambda')

hello()

print((lambda a,b: a-b)(7,5))

def func2(a):
    print(a)

func2((lambda a: f'{a}')('hello lambda'))
