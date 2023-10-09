from sys import stdin

df_c = 100
cnt = 0

n_str = stdin.readline()
nn = int(n_str)
N = list(map(int, n_str.strip()))
# print(N)
m = int(stdin.readline().rstrip())

if m !=0:
    b_lst = list(map(int, stdin.readline().rstrip().split(' ')))
else:
    b_lst = []
# 사용 가능한 채널리스트
c_lst = [i for i in range(10) if i not in b_lst]

# print(c_lst)

# + - 버튼만을 이용시 카운트 수
pm_cnt = abs(nn - df_c)

# 리모콘 숫자 버튼을 모두 누르지 못한다면
if m == 10:
    print(pm_cnt)
    exit()

# 버튼을 새로 누를때 누적합
f_n = 0

for i in range(len(N)):

    if N[i] in c_lst:
        # 만약 리모콘 버튼에 해당 수가 있다면
        f_n += N[i] * (10 ** (len(N) - 1 - i))
        # print(f'f_n: {f_n}')
    else:

        # 최소차
        min_dif = min(abs(x-N[i]) for x in c_lst)

        # 최소 차인 원소들로 리스트 만들기
        min_vals = [x for x in c_lst if abs(x-N[i]) == min_dif]

        # print(min_vals)
        # 만약 차가 동일한 원소들이 있을경우
        # 둘중 큰수로 만들수있는 최소수와
        # 작은 수로 만들수있는 최대수의 차를 이용해 수를 정한다.
        if len(min_vals) > 1:
            # 작은수로 만들수있는 최대수 min_m
            min_n = min_vals[0]*(10**(len(N)-1-i))
            # print(i)
            for j in range(len(N)-i):
                if j == len(N) - i - 1:
                    break
                min_n += max(c_lst)*(10**(len(N)-1-i-1-j))
            # print(f'min_n : {min_n}')
            # 큰수로 만들수있는 최소수와
            max_n = min_vals[1]*(10**(len(N)-1-i))
            for j in range(len(N) - i):
                if j == len(N) - i - 1:
                    break
                max_n += min(c_lst) * (10 ** (len(N) - 1 - i - 1 - j))
            # print(f'max_n : {max_n}')

            # 원래수 val
            val = nn-f_n
            # print(f'val : {val}')

            # 비교
            if max_n -val > val - min_n:
                f_n+=min_n
                break
            else:
                f_n+=max_n
                break

        # 만약 차가 동일한 원소들이 없을경우
        # 즉 len(min_vals)==1일경우
        else:
            if min_vals[0] < N[i]:
                f_n+=min_vals[0]*(10**(len(N)-1-i))
                for j in range(len(N) - i):
                    if j == len(N)-i-1:
                        break
                    f_n += max(c_lst) * (10 ** (len(N) - 1 - i - 1 - j))
                break
            else:
                f_n += min_vals[0] * (10 ** (len(N) - 1 - i))
                for j in range(len(N) - i):
                    if j == len(N)-i-1:
                        break
                    f_n += min(c_lst) * (10 ** (len(N) - 1 - i - 1 - j))
                break
print(f_n)
if len(str(f_n))+abs(f_n-nn) > pm_cnt:
    print(pm_cnt)
else:
    print(len(str(f_n))+abs(f_n-nn))