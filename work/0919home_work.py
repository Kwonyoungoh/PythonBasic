from sys import stdin
from random import *
# 가위 바위 보
# 0  1  2
name_lst = ['가위 🤞','바위 ✊','보 ✋']
# 무승부 패배 승리
# 3*3의 2차원 배열에 경우의 수 저장
# x = 유저의 결정 , y = 컴퓨터의 결정
# 배열 arr[x][y]
lst = [[0,1,2],[2,0,1],[1,2,0]]
# 가위 바위 보 승리 카운트 cnt
win_cnt = 0
play_cnt = 0

while win_cnt < 3:
    # 컴퓨터 먼저 결정
    comp = randint(0,2)
    # 플레이 카운트 증가
    play_cnt +=1

    print('가위: 0 바위: 1 보: 2 숫자로 입력하세요. : ', end='')
    # 사용자 입력받기
    usr = int(stdin.readline().rstrip())

    print('유저 :',name_lst[usr] , ' 컴퓨터 :',name_lst[comp])

    # if elif else 한번씩만 사용해서 풀이
    if lst[usr][comp] == 2:
        win_cnt += 1
        print('승리')
    elif lst[usr][comp] == 1:
        print('패배')
    else:
        print('무승부')

print(f'{play_cnt}번 후 승리')