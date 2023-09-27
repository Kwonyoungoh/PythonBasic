from sys import stdin
# 민감한 해빈이 문제

# 테스트 케이스 갯수
c = int(stdin.readline().rstrip())

for _ in range(c):
    # 의상 딕셔너리
    dic01 = {}
    # 의상의 수 n
    n = int(stdin.readline().rstrip())

    # 리스트로 받기
    for _ in range(n):
        lst = stdin.readline().rstrip().split(' ')
        # 키 확인 먼저
        if lst[1] in dic01:
            dic01[lst[1]].append(lst[0])
        else:
            dic01[lst[1]] = [lst[0]]
    t_c =1

    for i in dic01:
        t_c *= len(dic01[i])+1

    print(t_c-1)