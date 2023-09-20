import sys

# 26 5
# 와 같이 들어온다
inpt = sys.stdin.readline().rstrip()
args01 = inpt.split(' ')
mons_n01 = int(args01[0])
quiz_m01 = int(args01[1])
mon_lst=[]
mon_dic={}

for i in range(mons_n01):
    mon_n = sys.stdin.readline().rstrip()
    # 포켓몬을 mon_lst에 저장한다.
    mon_lst.append(mon_n)
    # 포켓몬을 dic 에 저장한다.
    mon_dic[mon_n] = i

# 문제를 받는다.
for _ in range(quiz_m01):
    quiz_n = sys.stdin.readline().rstrip()
    # 문제가 포켓몬이름인지 번호인지 판별 하도록하자
    # 포켓몬 이름은 무조건 도감에 있는 친구들만 들어온다.
    # 해당 판별 먼저하자
    if quiz_n.isalpha():
        print(mon_dic[quiz_n]+1)
    else:
        print(mon_lst[int(quiz_n)-1])