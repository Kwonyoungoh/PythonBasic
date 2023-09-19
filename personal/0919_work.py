from random import *
from sys import stdin
# 컴퓨터의 선택
comp = randint(0,3)

# 내선택
print('가위 : 0 바위 : 1 보 : 2')
lst= [0,1,2]
mine = int(stdin.readline().strip())
cnt =0
# 비긴경우
if lst[mine-comp] == lst[mine-1]:
    print('승리')
    cnt+=1
# 내가 이긴경우
# 가위 0 - 보 2 , 바위 1 - 가위 0 , 보 2 - 바위 1,
elif lst[mine-comp] == lst[mine+1]:
    print('패배')
# 내가 진경우
# 가위 0 - 바위 1, 바위 1 - 보 2 , 보 2 - 가위 0
else: