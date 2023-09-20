from functools import reduce

# 누적합에 대한 손쉬운 사용을 위해

a1 = [1, 2, 3, 4, 5]
a2 = {1, 2, 3, 4, 5}

def func1(x, y):
    return x + y

# reduce()는 무조건 2개의 인자를 받아야 한다
print(reduce(func1, a1))
# 이거 람다로 바꾸면?
print(reduce(lambda x,y: x+y, a1))
# set 도 됨
print(reduce(lambda x,y: x+y, a2))