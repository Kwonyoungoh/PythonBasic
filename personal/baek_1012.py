from sys import stdin

# 점검함수 chk(n,m)
def chk(x,y,farm):
    # 일단 0인친구는 패스
    for i in range(x):
        for j in range(y):
            if farm[i][j] == 0:
                continue
    # 만약 해당타일 4방향타일이 0이나 1이고 해당타일이 1이라면 2로 변경후
    # 리스트에 추가
    # 해당타일 주변에 2가있다면 해당타일이있는 리스트에 해당 타일을 추가 후 2로변경
    # 해당 리스트의 길이를 리턴



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

    # n*m인 밭을 먼저 만들자
    farm = [[0]*N for _ in range(M)]
    print(farm)
    # k개 만큼의 배추심기
    for _ in range(K):
        xy = list(map(int, stdin.readline().rstrip().split(' ')))
        farm[xy[0]][xy[1]] = 1

    # 각 밭에서 4방향으로 점검 함수

print(farm)