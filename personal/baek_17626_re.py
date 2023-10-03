from sys import stdin

# dp로 풀이

# 입력받기
n = int(stdin.readline().rstrip())

# n의 최대 갯수는 1^2으로만 표현될때 즉 최대 갯수는 n임
# 그렇다면 최소갯수는
dp = [0] * (n + 1)

for i in range(1, n + 1):
    min_val = n
    j = 1
    while j * j <= i:
        min_val = min(min_val, dp[i - j * j] + 1)
        j += 1
    dp[i] = min_val

print(dp[n])
