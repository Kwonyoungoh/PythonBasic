from sys import stdin

def f_way(x,y,farm):

    if x>0 and farm[x-1][y] == 2:
        return 1
    elif x < len(farm)-1 and farm[x+1][y] ==2:
        return 1
    elif y > 0 and farm[x][y-1] ==2:
        return 1
    elif y < len(farm[0])-1 and farm[x][y+1] ==2:
        return 1
    return 0

def f_way_c(x,y,farm):
    if x>0 and farm[x-1][y] == 1:
        farm[x-1][y] = 2
    if x < len(farm)-1 and farm[x+1][y] ==1:
        farm[x+1][y] = 2
    if y > 0 and farm[x][y-1] ==1:
        farm[x][y-1] = 2
    if y < len(farm[0])-1 and farm[x][y+1] ==1:
        farm[x][y+1] = 2

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
    for row in farm:
        print(row)
    for i in range(M):
        for j in range(N):
            if farm[i][j] == 0:
                continue

            farm[i][j] = 2
            if f_way(i,j,farm):
                continue
            else:
                f_way_c(i, j, farm)
                # print(i,j)
                cnt+=1

    print(cnt)
    # print(farm)

# 내일 dfs로 다시풀이하기