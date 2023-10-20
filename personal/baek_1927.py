from sys import stdin
import heapq
# 1927

n = int(stdin.readline().rstrip())
x = []

# 최대힙은 반대로 -로 저장해주면 간단히 구현된다.
# 기본적인구현
for _ in range(n):
    x_m = int(stdin.readline().rstrip())

    if x_m == 0:
        if not x:
            print(0)
            continue
        print(heapq.heappop(x))

    else:
        heapq.heappush(x,x_m)

