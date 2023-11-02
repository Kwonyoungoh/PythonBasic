from sys import stdin
from collections import deque
#1697
n,k = list(map(int,stdin.readline().rstrip().split(' ')))
cnt = 0
q = deque([n])
# k까지 가는 최단 거리
while q:
    for _ in range(len(q)):
        print(len(q))
        i = q.popleft()
        if i == k:
            break

        if i < k:
            q.append(i*2)
            q.append(i+1)
        else:
            q.append(i-1)
        print(q)
    cnt+=1

print(cnt)