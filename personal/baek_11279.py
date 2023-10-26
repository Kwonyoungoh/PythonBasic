from sys import stdin
import heapq
# 11279

mxh = []

n = int(stdin.readline().rstrip())

for _ in range(n):
    i = int(stdin.readline().rstrip())

    # 0이라면 제일 큰수 빼기
    if i == 0:
        print(-heapq.heappop(mxh)) if len(mxh) != 0 else print(0)
    else:
        heapq.heappush(mxh,-i)
