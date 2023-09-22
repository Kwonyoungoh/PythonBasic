from sys import stdin

# 2579
# 계단 갯수 받기
s_n = int(stdin.readline().rstrip())
lst01 = [0]
# 점수 입력 받기
for _ in range(s_n):
    point = int(stdin.readline().rstrip())
    lst01.append(point)


# 첫계단은 무조건 밟아야함
# 세계단 연속으로 밟을수는 없음

# 이전 계단 정보, 현재 계단 정보, 점수 리스트, 총합 점수 리스트, 현재까지의 점수 는 받아 줘야할거같음
def func(before, current, p_lst, t_lst, p):
    # 리턴 조건
    # 다음혹은 다다음 계단 마지막 계단이면
    # 마지막 계단 점수와 현재 계단 점수를 더하고
    # 점수 총합을 t_lst에 추가
    # 총합 점수 리스트를 리턴
    if (current + 1 == len(p_lst)-1) or (current + 2 == len(p_lst)-1):
        p = p + p_lst[current] + p_lst[len(p_lst)-1]
        t_lst.append(p)
        return t_lst

    # 0계단은 무조건 포함
    # 이전계단이 없다면
    # 포인트에 첫계단 점수 더해주고
    # if before == 0 and current == 0:
    #     p += p_lst[before]

    # 재귀 호출
    # 이전 계단이 한계단 전 이라면 다음 계단 선택은 패스
    # 근데 이전 계단이 0번째 계단이면 ㄱㅊ
    # 다음 계단 선택
    if current - 1 != before or current == 0 or current == 1:
        # 일단 현재까지점수(p)에 현재 계단점수를 더해준다
        func(current, current + 1, p_lst, t_lst, p + p_lst[current])

    # 다다음 계단 선택
    func(current, current + 2, p_lst, t_lst, p + p_lst[current])


ans_lst = []
ans = func(0, 0, lst01, ans_lst, 0)

print(sorted(ans_lst,key = lambda x : -x )[0])
