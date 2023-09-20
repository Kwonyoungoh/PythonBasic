def int_func(a: int):
    return a + 1


print(int_func(2))


# 리턴 타입의 명시도 가능하다.
# 리턴 타입 같은 경우 강제성은 없다.
def func2(a: int, b: str) -> str:
    return 'sdfdf'

print(func2(1,'dfd'))