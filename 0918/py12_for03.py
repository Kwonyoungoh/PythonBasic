# for ~ break

# for i in range (0,5):
#     print(i)
#     if i == 2:
#         break

# 점수 5개를 받은 뒤 5개의 점수 모두 40점 이상 평균 60점 이상

cnt = 5
total = 0

for i in range(cnt):
    score = int(input())
    if score < 40:
        print('불합격')
        break
    total += score
    if i == 4:
        avg = total // 5
        print('평균 : ', avg)
        print('합격' if avg >= 60 else '불합격')
