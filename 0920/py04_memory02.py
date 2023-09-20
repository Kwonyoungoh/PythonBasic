def test1(a):
    a += 10


a = 1
test1(a)
print(a)


def test2(b):
    b[0] = 'zzz'


def test3(a):
    b = (1, 2, 3)
    print(id(a))
    print(id(b))
    return a is b


def test4(a):
    print(id(a))
    b = {1, 2, 3}
    print(id(b))
    return a is b


b = ['aaa']
test2(b)
print(b)

a = (1, 2, 3)
a1 = {1, 2, 3}

print(test3(a))
print(test4(a1))
