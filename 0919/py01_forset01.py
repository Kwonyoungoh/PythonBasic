lst1 = [2 + x for x in range(5)]
print(lst1)


def func(x):
    return x + 2


# set comprehension 도 가능하다.
# 함수 사용도 가능함
set1 = {func(x) for x in range(5)}
print(set1)
