from sys import stdin

# 1389

# 최단거리 구하기
def bfs(sn,tn,lst):
    # 시작노드에서 1인친구만 큐에 넣기
    q = []
    vs=[0]*len(lst)
    vs[sn] = 1
    if lst[sn][tn] == 1:
        return 1

    for i in range(len(lst)):
        if lst[sn][i] == 1:
            q.append(i)


    while len(q) != 0:
        n = q.pop()
        if lst[n][tn] ==1:
            return ;
        for i in range(len(lst)):
            if lst[n][i] == 1 and vs[i] != 1:
                vs[i] = 1
                q.append(n)


# 케빈 베이컨의 수
# 각 인덱스 도달까지의 단계의 합이 가장적은사람을 구하는 프로그램

# 관계 리스트 리스트, 시작노드, 타겟노드, 카운트

n,m = list(map(int,stdin.readline().rstrip().split(' ')))

lst = [ [0]*n for _ in range(n)]

for _ in range(m):
    x,y = list(map(int,stdin.readline().rstrip().split(' ')))
    lst[x-1][y-1] = 1
    lst[y-1][x-1] = 1