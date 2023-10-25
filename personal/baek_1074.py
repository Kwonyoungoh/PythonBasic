from sys import stdin
# 1074

# DFS 인줄
# 재귀
def self_z(n,x,y,val,c,r):

    if n==1:
        if x == c and y == r:
            return val[0]
        val[0] += 1
    else:
    # 계속 넷으로 나눈다
        res = self_z(n//2,x,y,val,c,r)
        if res is not None:
            return res

        res = self_z(n//2,x+n//2,y,val,c,r)
        if res is not None:
            return res

        res = self_z(n//2,x,y+n//2,val,c,r)
        if res is not None:
            return res

        res = self_z(n//2,x+n//2,y+n//2,val,c,r)
        if res is not None:
            return res


# n r c
nrc = list(map(int,stdin.readline().rstrip().split(' ')))

N = nrc[0]
r = nrc[1]
c = nrc[2]

# lst = [0]*(2**N)
# ans = [[0] * (2**N) for _ in range(2**N)]
val1 = [0]
# 방문순서
# 걍 N*N을 방문순서대로 1부터 넣자


print(self_z(2**N,0,0,val1,c,r))