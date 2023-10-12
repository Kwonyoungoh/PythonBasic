from sys import stdin
from collections import deque

def dfs (cn,lst,ans,vs):

    if vs[cn] == 0 :
        return

    if cn not in ans:
        ans.append(cn)

    if lst[cn] == 0:
        return
    vs[cn]=0
    for i in lst[cn]:
        dfs(i,lst,ans,vs)

def bfs (cn,lst,ans):

    # 일단 시작 노드 방문
    # 해당 노드 간선들 순차적으로 방문
    ans.append(cn)
    # 방문 확인 리스트
    vs = [0]+[1]*(len(lst)-1)
    #방문해야할 노드 리스트
    q = deque()

    if lst[cn] == 0:
        return

    for i in lst[cn]:
        q.append(i)
        vs[i] = 0
        ans.append(i)
    # 큐가 비어있지않은 동안
    while q:
        nn = q.popleft()
        # 시작 노드 간선 부터 넣은 후 시작

        for i in lst[nn]:
            if vs[i] == 0:
                continue
            q.append(i)
            vs[i] = 0
            if i not in ans:
                ans.append(i)




# 입력
str = list(map(int,stdin.readline().rstrip().split(' ')))

n = str[0]
m = str[1]
v = str[2]

# 2차원 형태로 저장
lst = [0]*(n+1)

for _ in range(m):
    inpt = list(map(int,stdin.readline().rstrip().split(' ')))

    if isinstance(lst[inpt[0]],list):
        lst[inpt[0]].append(inpt[1])
    else:
        lst[inpt[0]] = [inpt[1]]

    if isinstance(lst[inpt[1]], list):
        lst[inpt[1]].append(inpt[0])
    else:
        lst[inpt[1]] = [inpt[0]]

    lst[inpt[0]].sort()
    lst[inpt[1]].sort()


# DFS 부터
ans=[]
vs = [0]+[1]*(len(lst)-1)

dfs(v,lst,ans,vs)
print(*ans)

ans2 = []
bfs(v,lst,ans2)
print(*ans2)