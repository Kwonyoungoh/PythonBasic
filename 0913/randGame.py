from random import *

# 임의의 숫자
# 입력 숫자
# 랜덤한 숫자와 입력숫자


while True:
    try:
        num: int = int(input('0부터 100까지의 숫자 중 하나를 입력해주세요 :'))

        if 0 <= num <= 100:
            print('입력 숫자: {num}')
            break
        else:
            print('0부터 100 사이의 정수를 입력해주세요')
    except ValueError:
        print('정수만 입력하세요')

i: int = randrange(0, 100)
print(f'임의의 숫자 : {i}')

print(f'{num} {i}')

ans: int = randrange(1)
print('정답 : ', end='')
if ans == 0:
    print('짝')
else:
    print('홀')

if num % 2 == ans and i % 2 == ans:
    print('무승부')
elif num % 2 == ans:
    print('플레이어 승리!')
elif i % 2 == ans:
    print('컴퓨터 승리!')
else:
    print('모두 패배')
