from sys import stdin
# 2606
# 바이러스

# dfs 인듯?
def self(lst,n):
    for i in lst[n]:
        if chk_lst[i] == 0:
            chk_lst[i] = 1
            self(lst,i)


# 컴퓨터의 수 n
n = int(stdin.readline().rstrip())

# 컴퓨터의 번호 쌍 m
m = int(stdin.readline().rstrip())

lst = [[] for _ in range(n+1)]

# 번호쌍 입력
for _ in range(m):
    input_lst = sorted(stdin.readline().rstrip().split(' '))
    # 각 번호별 연결 노드들을 리스트의 리스트로 정렬
    a, b = map(int, input_lst)
    lst[a].append(b)
    lst[b].append(a)

chk_lst = [0]*(n+1)
chk_lst[1] = 1

# 1과 연결된 노드들만 확인
# 다시 해당 노드들과 연결된 노드들 확인
# 전부 visted 마킹 해주고
# visted한 노드 갯수만 구한다면
# 바이러스 갯수 출력이 가능핟.
self(lst,1)

print(sum(chk_lst)-1)
