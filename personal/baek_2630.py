from sys import stdin
# 2630

# 지름 n, 시작지점
def dfs(lst,n,s_x,s_y,cnt):
    flag = False

    # 주어진 정사각형 구성 갯수만큼 반복
    for i in range(n):
        for j in range(n):
            # 0으로 시작
            if lst[s_x][s_y]==0:
                if n == 1:
                    cnt[0]+=1
                    break

                if lst[s_x+i][s_y+j]!=0:
                    flag = True
                    break
                elif i == n-1 and j == n-1:
                    cnt[0] += 1
            # 1로 시작
            if lst[s_x][s_y]==1:
                if n == 1:
                    cnt[1]+=1
                    break


                if lst[s_x+i][s_y+j]!=1:
                    flag = True
                    break
                elif i == n-1 and j == n-1:
                    cnt[1] += 1
        if flag:
            break
    # print(n)
    if flag:
        dfs(lst, int(n / 2), s_x, s_y,cnt)
        dfs(lst, int(n / 2), s_x + int(n / 2), s_y,cnt)
        dfs(lst, int(n / 2), s_x, s_y + int(n / 2),cnt)
        dfs(lst, int(n / 2), s_x + int(n / 2), s_y + int(n / 2),cnt)
    # print(cnt)



n = int(stdin.readline().rstrip())
nn = []
# 2차 배열 생성
for _ in range(n):
    n_lst = list(map(int,stdin.readline().rstrip().split(' ')))
    nn.append(n_lst)

# n/2로 일단 자르고
# 각 요소가 전부 같은 색인지 확인
# 같은 색이 아니라면 다시 나누고
# 확인 다 같은 색일때까지 반복
# dfs
cnt =[0,0]
dfs(nn,n,0,0,cnt)
print(cnt[0])
print(cnt[1])