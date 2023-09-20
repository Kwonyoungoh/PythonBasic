def func1(x,y):
    return x+y,x-y

def func2(x,y):
    return x+y,x-y,x*y

# 리턴이 두개가 된다.
x1 = func1(20,10)

# 튜플형태로 반환된다...ㄷㄷ
print(x1)

x2,  y2  = func1(10,20)
print(x2)
print(y2)

# 언패킹을 이용한다면?
x3, *y3 = func2(10,20)
print(x3)
print(y3)