from sys import stdin
# 1764
# 듣도 보도 못한 사람

# 듣도 못한 사람 n
# 보도 못한 사람 m

input01 = stdin.readline().rstrip()

input_lst = input01.split(' ')

n = int(input_lst[0])
m = int(input_lst[1])

n_set = set()
m_set = set()

for _ in range(n):
    n_name = stdin.readline().rstrip()
    n_set.add(n_name)

for _ in range(m):
    m_name = stdin.readline().rstrip()
    m_set.add(m_name)

ans_set = n_set & m_set
print(len(ans_set))

# 사전순정렬

ans = sorted(list(ans_set), key = lambda x : x)

for name in ans:
    print(name)
