from sys import stdin

n = int(stdin.readline().rstrip())
m = int(stdin.readline().rstrip())
# 일단 최댓값
ans = abs(100-n)
if m == 10:
    print(ans)
    exit()
# 고장난 버튼 리스트
elif m==0:
    b_lst =[]
else:
    b_lst = list(map(str,stdin.readline().rstrip().split(' ')))

# 브루트 포스로 모든 경우의 수를 찾아보자
for i in range(1000001):
    for j in str(i):
        if j in b_lst:
            break

    else:
        ans = min(ans,len(str(i))+abs(i-n))

print(ans)