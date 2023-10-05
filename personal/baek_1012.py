from sys import stdin
from sys import setrecursionlimit
setrecursionlimit(10000)
def f_way_c(x,y,farm):
    if x>0 and farm[x-1][y] == 1:
        farm[x-1][y] = 2
        f_way_c(x-1, y, farm)
    if x < len(farm)-1 and farm[x+1][y] ==1:
        farm[x+1][y] = 2
        f_way_c(x+1, y, farm)
    if y > 0 and farm[x][y-1] ==1:
        farm[x][y-1] = 2
        f_way_c(x, y-1, farm)
    if y < len(farm[0])-1 and farm[x][y+1] ==1:
        farm[x][y+1] = 2
        f_way_c(x, y+1, farm)

# 다 필요없고 4방향모두 2가아니라면 cnt + 1
# 테스트 케이스 갯수
T = int(stdin.readline().rstrip())

# 배추를 심은 배추밭의 가로길이 M
# 세로길이 N
# 배추 갯수 K
for _ in range(T):
    mnk = stdin.readline().rstrip().split(' ')

    M = int(mnk[0])
    N = int(mnk[1])
    K = int(mnk[2])
    cnt = 0
    # n*m인 밭을 먼저 만들자
    farm = [[0]*N for _ in range(M)]

    # k개 만큼의 배추심기
    for _ in range(K):
        xy = list(map(int, stdin.readline().rstrip().split(' ')))
        farm[xy[0]][xy[1]] = 1

    for i in range(M):
        for j in range(N):
            if farm[i][j] == 0 or farm[i][j] == 2:
                continue

            if farm[i][j] == 1:
                cnt += 1
            # 해당 타일에 연결된 모든 타일을 2로 만들기
                f_way_c(i, j, farm)


    print(cnt)

# 내일 dfs를 추가
# 해당좌표 가 1이면
# 해당좌표와 4방향으로 연결된 모든 타일을 연속해서 2로 만듦
# 그렇다면 1을 발견할때만 cnt +1을 해주면된다.
# 배추를 심은 좌표리스트를