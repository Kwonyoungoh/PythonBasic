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
    # 해당 범위 안에 있는 c r만 탐색하도록 변경해야할듯...
    # 계속 넷으로 나눈다
        if c < x+n//2 and r < y+n//2:
            res = self_z(n//2,x,y,val,c,r)
            if res is not None:
                return res
        else:
            # print(val[0])
            val[0] += (n//2)**2

        if c >= x+n//2 and r < y+n//2:
            res = self_z(n//2,x+n//2,y,val,c,r)
            if res is not None:
                return res
        else:
            # print(val[0])

            val[0] += (n//2)**2

        if  c < x+n//2 and r >= y+n//2:
            res = self_z(n//2,x,y+n//2,val,c,r)
            if res is not None:
                return res
        else:
            # print(val[0])

            val[0] += (n//2)**2

        res = self_z(n//2,x+n//2,y+n//2,val,c,r)
        if res is not None:
            return res
        # print(val[0])

        val[0] += (n//2)**2


# n r c
n,r,c = list(map(int,stdin.readline().rstrip().split()))
# print(n,r,c)
# N = nrc[0]
# r = nrc[1]
# c = nrc[2]

# lst = [0]*(2**N)
# ans = [[0] * (2**N) for _ in range(2**N)]
val1 = [0]
# 방문순서
# 걍 N*N을 방문순서대로 1부터 넣자


print(self_z(2**n,0,0,val1,c,r))