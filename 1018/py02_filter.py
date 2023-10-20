# 1. 아이템마다 적용시킬 함수

def is_even(n):
    return True if n%2 == 1 else False

tar =range(1,11)

# 이게 for문 보다 빠를듯?
res2 = filter(lambda x: x%2==0, tar)
res3 = map(lambda x: x%2==0, tar)

print(*list(res2))
print(*list(res3))