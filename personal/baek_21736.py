from sys import stdin,setrecursionlimit
setrecursionlimit(1000000)
# 21736

# 헌내기는 친구가 필요해

n,m = map(int, stdin.readline().rstrip().split(' '))

def dfs (lst,ipos,cnt,n,m):
    x,y = ipos
    # 사람이면 카운트 증가
    if lst[x][y] == 'P':
        cnt[0]+=1
    # 탐색한 위치는 숫자 0으로 변경
    lst[x][y] = 0
    # 4방향으로 탐색한다.
    if 0< x+1 < n:
        dfs(lst, [x + 1, y],cnt,n,m) if lst[x + 1][y] != 'X' and lst[x + 1][y] != 0 else 0
    if 0 <= x-1 < n:
        dfs(lst, [x - 1, y], cnt,n, m) if lst[x - 1][y] != 'X' and lst[x - 1][y] != 0 else 0
    if 0 < y+1 < m:
        dfs(lst, [x, y + 1], cnt,n, m) if lst[x][y + 1] != 'X' and lst[x][y + 1] != 0 else 0
    if 0 <= y-1 < m:
        dfs(lst, [x, y - 1], cnt,n, m) if lst[x][y - 1] != 'X' and lst[x][y - 1] != 0 else 0
# I 가 있는 지점부터 차근차근 계속 탐색해서 P가 있으면 cnt+1
# X가 있으면 해당 타일의 사방향은 탐색안함

# 일단 입력 받아서 2차행렬을 만들자

# lst = [list(stdin.readline().rstrip()) for _ in range(n)]

lst = []
ipos = []
# 일단 i의 위치를 받아야함
for i in range(n):
    str =list(stdin.readline().rstrip())
    if 'I' in str:
        ipos = [i,str.index('I')]

    lst.append(str)

cnt = [0]
# 이제 i의 위치를 중심으로 탐색
dfs(lst,ipos,cnt,n,m)

print( cnt[0] if cnt[0] >0 else 'TT')