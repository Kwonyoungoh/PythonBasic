from random import *
# 1. 사용자에게 두 개의 정수를 입력 받아, 두 정수 중에서 큰 수를 출력하는 프로그램을 작성하세요. 만
# 약 두 수가 같다면, "두 수는 같습니다"라는 메시지를 출력하세요.

# a1 = int(input('number 1 : '))
# b1 = int(input('number 2 : '))

# print('Same' if a1 == b1 else 'Diff')

# 2 시험점수

def grade (score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return  'D'
    else:
        return  'F'

# score1 = int(input())

# print(grade(score1))

# 3 해당 리스트중 홀수만 출력
nums = list(range(1,11))
print( [i for i in nums if i%2])

# 4-1
# cnt = int(input())
lst1 = []

# for _ in range(cnt):
#     num = int(input())
#     lst1.append(num)

sum1 = sum(lst1)

# print('sum : ',sum1)
# print(f'avg : { sum1/cnt : .2f}')

# 4-2

lst2 = []

# while True:
    # num = int(input(' input number(0 is quit) : '))

    # if num == 0:
    #     break
    #
    # lst2.append(num)

sum2 = sum(lst2)
# print(f'sum : {sum2}')
# print(f'sum : {sum2/len(lst2) : .2f}')

# 응용문제 1
# 문자열 리스트화 시키기

str01 = 'apple ant banana acorn'

lst01 = str01.split(' ')
print(lst01)
cnt01 =0

for n in lst01:
    if n[0] == 'a':
        cnt01 += 1

print(cnt01)

# 람다 함수 를 통한 리스트 정렬

lst02 = [ randint(1,100) for i in range(10)]
print(lst02)

# 짝수 홀수 나눠서 짝수는 오름차순 홀수는 내림차순
print( sorted(lst02,key= lambda x: ( x%2-1 , x if x%2-1 else -x )) )

# 무작위 lst2 집합에서 짝수만
print([lst02[x] for x in range(len(lst02)) if not lst02[x]%2])