from sys import stdin

# 최대점수 dp[i]

n = int(stdin.readline().rstrip())

plst = [0] + [int(stdin.readline().rstrip())for _ in range(n)]
dp = [0]*(n+1)

if n >= 1:
    dp[1] = plst[1]
if n >=2:
    dp[2] = plst[1]+plst[2]


for i  in range(3,n+1):
    dp[i] = max(dp[i-3]+plst[i-1]+plst[i],dp[i-2]+plst[i])

print(dp[n])