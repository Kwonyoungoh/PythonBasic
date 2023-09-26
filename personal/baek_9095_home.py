from sys import stdin


# 테스트 케이스 갯수 T
T = int(stdin.readline().rstrip())

# 정수 n 리스트
n_lst = [int(stdin.readline().rstrip())for _ in range(T)]

# n = a*1 + b*2 + c*3

# 중복 계산이 뭐가 있을까?
def get_cases(n):
# 일반적인 해결책
# 1이 n만큼 들어가는 조합부터
# 3이 n//3만큼 들어가는 조합까지
# n//3 < a+b+c < n
# n=1이면
    dp = [0,1,2,4]

    if n < 4:
        return dp[n]

    for i in range(4,n+1):
        dp.append(dp[i-1] + dp[i-2] +dp[i-3])

    return dp[n]

for i in n_lst:
    print(get_cases(i))