# 다른 언어는 이런식이다.
# for( int i; i < 10; i++){
#  ...  반복할 문장
# }

# 그러나 파이썬의 for문은 이런식으로 동작하지 않는다.

# python for문
# for 변수 in 리스트 (또는 튜플이나 or 문자열) : 열거가능한 내용 즉 멀티플라이어
# ... 반복할 문장

# 리스트 반복
list1 = ['Naver', 'Kakao', 'SK C&C', 'KT']

# 다른 열거 가능한 자료형들 멀티플라이어들도 가능하다
# 튜플
i = 0
while i < len(list1):
    print(list1[i])
    i += 1

for val in list1:
    print(val)

dic1 = {'Naver': 10, 'Kakao': 7, 'SK C&C': 5, 'KT': 2}

for val in dic1:
    print(dic1[val])
# 그렇다면 val와 key값 모두 필요하다면?
for key, val in dic1.items():
    print(f'{key} {val}')

# 빠른 연산을 위해선
for val in dic1.values():
    print(val)

print(dic1.values())

# for에 대한 예외처리
for i in []:
    print(i)
else:
    print('no data')

# 멀티플라이어 조합
list7 = [(1, 2), (3, 5), (2, 5), (7, 1), (8, 2)]
for (first, second) in list7:
    print(f'{first} {second}')
