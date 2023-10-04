from sys import stdin

n = int(stdin.readline().rstrip())

dp = [0,1]

# 0의 제곱은 계산 할 필요가 없다
sqs = [i*i for i in range(1,int(n**0.5)+1)]

for i in range(2,n+1):
    min_v = n

    for sq in sqs:
        if sq > i:
            break
        min_v = min(min_v,dp[i-sq]+1)

    dp.append(min_v)

print(dp[n])