a = 10
b = 11
c = 12
d = 12
# 식별자가 보는 주솟값을 가르킨다.
print(a, ':', id(a))
print(b, ':', id(b))
print(c, ':', id(c))
print(d, ':', id(d))

print('같은 객체' if c is d else '다른 객체')