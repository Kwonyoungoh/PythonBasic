from sys import stdin
# 11659
# 구간합

inpt1 = stdin.readline().rstrip().split(' ')

# 수열 길이
n = int(inpt1[0])
# 문제 수
m = int(inpt1[1])

# 수열 입력 받기
lst01 = list(map(int,stdin.readline().rstrip().split(' ')))
inpt3 = []
dp_sum = []
# 문제들 입력
for _ in range(m):
    inpt3.append(list(map(int,stdin.readline().rstrip().split(' '))))

# 부분합들 계산
for i in range(len(lst01)):
    if i == 0:
        dp_sum.append(lst01[i])
        continue

    dp_sum.append(lst01[i] + dp_sum[i-1])

dp_sum = [0]+dp_sum

for c in inpt3:
    # [x,y]
    # y까지의 부분합에서 x-1까지의 부분합을 빼주자
    print(dp_sum[c[1]]-dp_sum[c[0]-1])