from sys import stdin, setrecursionlimit
# 11724
setrecursionlimit(1000000)
# 방향없는 그래프

# 정점의 갯수 N
# 간선수 M

n,m = map(int,stdin.readline().rstrip().split(' '))

def dfs(g,visited,snode):

    # 방문 노드리스트 켜주고
    visited[snode] = 1
    # 방문 노드 간선 꺼주기
    # 이미 방문한 노드면 꺼주기
    for i in range(len(g[snode])):
        if g[snode][i] == 1:
            g[snode][i] = 0
            # 이미 방문한 노드가 아니라면
            # 방문하겠다.
            if visited[i] == 0:
                dfs(g,visited,i)


#우선 그래프를 표현
g = [[0]*n for _ in range(n)]

for _ in range(m):
    u,v = map(int,stdin.readline().rstrip().split(' '))

    g[u-1][v-1] = 1
    g[v-1][u-1] = 1


v_lst=[0]*n
cnt = 0
for i in range(n):
    if v_lst[i] == 0:
        cnt += 1
        dfs(g,v_lst,i)


print(cnt)