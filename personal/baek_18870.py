from sys import stdin,setrecursionlimit
setrecursionlimit(1000000)
# 18870

# 좌표압축

n = int(stdin.readline().rstrip())
lst = list(map(int, stdin.readline().rstrip().split(' ')))
h = sorted(list(set(lst)))

# 딕셔너리 쓰자 해시테이블 써서 더빠름

h_d = {j:i for i,j in enumerate(h)}
# 최소 숫자 부터 0 을 주는 방식으로 교체

lst=[h_d[i] for i in lst]

print(*lst)