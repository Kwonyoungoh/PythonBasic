from sys import stdin
# 11399
# 인하은행
# N명의 사람들 n번째 사람은 t1의 시간만큼

# 주어지는 사람수
n  = int(stdin.readline().rstrip())

# 시간의 배열 nums
# map 의 사용법 잘 숙지하셈
nums = list(map( int , stdin.readline().rstrip().split(' ')))

# 시간의 배열을 최솟값부터 정렬
# 그래야 작은 시간 이 제일 많이 중복되기 때문.
s_nums = sorted(nums)

# c_t 으로 현재 시간
# t_t 으로 전체 시간 총합
# b_t 이전 까지의 시간
c_t=t_t=b_t = 0

# s_nums의 길이만큼 반복
for n in s_nums:
    c_t = b_t + n
    b_t += n
    t_t += c_t

print(t_t)