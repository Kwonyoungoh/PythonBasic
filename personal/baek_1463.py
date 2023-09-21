from sys import stdin


# 1만들기
# 3으로 나누기
# 2로 나누기
# 1빼기

# 시간복잡도를 생각하지말고 해보자
# 최소 횟수로 하려면?
# 큰수 부터 나눠 주는게 좋다
# 최소 횟수
# dfs
# 바텀업방식
# 최소한의 연산으로
# 주어진 숫자 n까지
def dfs(n, cnt):
    if n == 1:
        return cnt

    min_cnt = float('inf')

    if n % 3 == 0:
        min_cnt = min(min_cnt, dfs(n // 3, cnt + 1))
    if n % 2 == 0:
        min_cnt = min(min_cnt, dfs(n // 2, cnt + 1))
    min_cnt = min(min_cnt, dfs(n - 1, cnt + 1))

    return min_cnt


# memoization 메모이제이션을 이용하자
def func1(n):
    lst1 = []
    # 주어진 숫자 n번만큼 반복한다.
    for i in range(n-1):
        # 다 저장하자
        # 리스트도 초기화 해둬야함
        # 1일때
        lst1.append(0)
        if i == 0 or i == 1 or i == 2:
            lst1[i] = 1
            continue

        if (i + 1) % 3 == 0:
            if lst1[i]:
                lst1[i] = min(lst1[i], lst1[(i + 1) // 3] + 1)
            else:
                lst1[i] = lst1[lst1[(i + 1) // 3]] + 1

        if (i + 1) % 2 == 0:
            if lst1[i]:
                lst1[i] = min(lst1[i], lst1[(i + 1) // 2] + 1)
            else:
                lst1[i] = lst1[lst1[(i + 1) // 2]] + 1

        if lst1[i]:
            lst1[i] = min(lst1[i], lst1[(i + 1) - 1] + 1)
        else:
            a= lst1[lst1[(i + 1) - 1]]
            lst1[i] = a + 1

    print(lst1[n-1])


n = int(stdin.readline().rstrip())
func1(n)


# 10 5 4 2 1
# 10 9 3 1
# 16 15 5 4 2 1
# 16 8 4 2 1
