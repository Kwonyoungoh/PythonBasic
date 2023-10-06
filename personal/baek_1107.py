from sys import stdin, setrecursionlimit

df_c = 100
n = int(stdin.readline().rstrip())
m = int(stdin.readline().rstrip())

b_lst = list(map(int, stdin.readline().rstrip().split(' ')))
# 사용 가능한 채널리스트
c_lst = [i for i in range(10) if i not in b_lst]

print(c_lst)
# 먼저 n 에 가장 가까운 채널로 이동해야함
# 그렇다면 몇자리 숫자인지