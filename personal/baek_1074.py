from sys import stdin
# 1074

# DFS 문제

# n r c
nrc = list(map(int,stdin.readline().rstrip().split(' ')))

n = nrc[0]
r = nrc[1]
c = nrc[2]

lst = [0]*(2**n)
ans = []
for i in range(2**n):
    ans.append(lst)
print(ans)
# 방문순서
# 걍 N*N을 방문순서대로 1부터 넣자

for i in range((2**n)**(2**n)):
