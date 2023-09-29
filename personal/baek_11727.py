from sys import stdin
# 11727

n = int(stdin.readline().rstrip())

# 방법의 수
# 구하기     20  11 21
lst = [0,1,3,5]
# dp[x] =

if n < 4:
    print(lst[n])
else:
    for i in range(4,n+1):

        lst.append(lst[i-1]+2*lst[i-2])

    print(lst[n]%10007)