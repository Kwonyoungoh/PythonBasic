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

# 그러나 배열에서는 다른객체다 왤까?
# 리스트같은 경우는 가변(mutable)이기 때문에 다른주소 같은 값을 바라보더라도
lst1 = [1, 2, 3]
lst2 = [1, 2, 3]
print('같은 객체' if lst1 is lst2 else '다른 객체')
print(id(lst1))
print(id(lst2))

# 그러나 튜플에서는 같은객체다
# 결국 immutable이기때문에 같은 주소를 가진다.
lst1 = (1, 2, 3)
lst2 = (1, 2, 3)
print('같은 객체' if lst1 is lst2 else '다른 객체')
print(id(lst1))
print(id(lst2))
