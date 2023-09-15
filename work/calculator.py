# 학점계산기
# 1. 1~100 사이의 정수를 입력받는다.
# 2. 점수의 범위에 따라서 각가 학점을 A B C D F 로 출력
# 100 - 90 90 - 80 80 -70

score = int(input('내 점수 : '))

if 100 > score >= 90 :
    score = 'A'
elif score >= 80:
    score = 'B'
elif score>=70:
    score = 'C'
else:
    score = 'D'

print(score)