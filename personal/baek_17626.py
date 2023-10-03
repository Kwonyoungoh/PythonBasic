from sys import stdin
# 17626

n = int(stdin.readline().rstrip())

# 해당 n을 최소한의 제곱수의 합으로 표현하시오

# n과 가장 가까운 제곱수를 구하고 빼준다
# 해당 과정을 반복

def func1(n,t):
    for i in range(50):
        if n-(t-i)**2 >= 0:
            print(t-i)
            return n-(t-i)**2


cnt = 0

while True:
    if n == 0:
        print(cnt)
        break

    # n은 우선 224^2 보다 클수없다.
    # 200부터
    if n >=(200**2):
        n = func1(n,223)
        cnt+=1
    elif n >= (150**2):
        n = func1(n, 200)
        cnt += 1
    elif n >= (100**2):
        n = func1(n, 150)
        cnt += 1
    elif n>= (50**2):
        n = func1(n, 100)
        cnt += 1
    else:
        n = func1(n, 50)
        cnt += 1

# 해당방법은 1^2을 여러번 사용할가능성이 높다
# 그리디 알고리즘이란?
# 주어진 상황에서의 최적의 해를 찾는것을 반복
# 그러나 해당 방법이 항상 최적해를 찾아 줄리는 없다.
# 자 그렇다면 dp로 풀도록하자
