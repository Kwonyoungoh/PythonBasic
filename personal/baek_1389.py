from sys import stdin
from collections import deque
import heapq
# 1389

# 최단거리 구하기
def bfs(sn, tn, lst):
    # 시작노드에서 1인친구만 큐에 넣기
    q = deque([sn])
    vs = [0] * len(lst)
    vs[sn] = 1
    cnt = 0

    while q:
        size = len(q)
        # 다음 레벨의 노드로 이동할 때 카운터 증가
        cnt += 1
        for _ in range(size):
            n = q.popleft()
            if n == tn:
                return cnt - 1
            for i in range(len(lst[n])):
                if lst[n][i] == 1 and vs[i] == 0:
                    vs[i] = 1
                    q.append(i)


# 케빈 베이컨의 수
# 각 인덱스 도달까지의 단계의 합이 가장적은사람을 구하는 프로그램

# 관계 리스트 리스트, 시작노드, 타겟노드, 카운트

n, m = list(map(int, stdin.readline().rstrip().split(' ')))

lst = [[0] * n for _ in range(n)]

for _ in range(m):
    x, y = list(map(int, stdin.readline().rstrip().split(' ')))
    lst[x - 1][y - 1] = 1
    lst[y - 1][x - 1] = 1

# 최단 거리를 구하는 식은 찾았으니 각 인덱스에서 인덱스까지의 거리를 합산하는 로직작성
ans = []
for i in range(len(lst)):
    cnt = 0
    for j in range(len(lst)):
        cnt+=bfs(i,j,lst)

        if j == (len(lst)-1):
            ans.append(cnt)

print(ans.index(min(ans))+1)