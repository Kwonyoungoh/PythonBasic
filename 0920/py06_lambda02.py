from sys import stdin


# map 함수
def func1(x):
    return x * 2


# 이러면... for문을 안 돌려줘도 된다..!!!!!!!
list1 = list(map(func1, [1, 2, 3, 4]))
print(list1)

list2 = list(map(lambda x: x * 2, [1, 2, 3, 4]))
print(list2)

# 로직 풀때 이런식으로 int형으로 받는다면 으로
# 많이 쓰인다.
# T = int(stdin.readline().rstrip())
# for i in range(T):
#     a,b = map(int,stdin.readline().split())

# 1
dic1 = {1: 10, 2: 20, 3: 30}
list2 = list(map(func1, [dic1[i] for i in dic1]))
print(list2)

# 2 람다사용시
print(list(map(lambda x: x * 2, [1, 2, 3])))

# 3 lambda와 map 모든걸 조합한 다면?
a3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(map(lambda x: str(x) if x % 3 == 0 else x, a3)))

# 예능
a4 = [1, 2, 3, 4, 5]
b4 = [2, 4, 6, 8, 10]

# 왜냐면 파이썬은 실제 서비스를 만들기보단
# 본인이 사용하는 코드를 사용하기위해
# 이런식으로 사용하기도 한다.
print(list(map(lambda x, y: x * y, a4, b4)))
