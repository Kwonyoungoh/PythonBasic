from sys import stdin

# 2805

nm = list(map(int,stdin.readline().rstrip().split(' ')))

# 나무수
n = nm[0]
# 필요한 나무의 미터수
m = nm[1]

# 나무의 높이 리스트
t_lst = list(map(int,stdin.readline().rstrip().split(' ')))

# 나무를 최대한 적은 길이 만큼만 자르고싶다.
l = 0
r = max(t_lst)
ans = 0
while l<=r:
    # 우선 중간 값을 구하고
    mid= (r+l)//2
    # 토탈길이를 구함
    s = sum(t-mid if t-mid > 0 else 0 for t in t_lst)

    # 자른 나무의 총합이 s고 필요길이 보다 크다면
    if s >= m:
        ans = mid
        l = mid+1
    else:
        r = mid -1

print(ans)