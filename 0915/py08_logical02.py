a1 = 50
# 조합 연산자
print(a1 > 10 and a1 < 100)
# 파이썬은 조건식을 연달아 걸 수 있다.
print(10 < a1 < 100)

print('-' * 40)

a2 = 10
print(bool(a2))

b1 = ['a']
b2 = ['b']
# 데이터의 유무를 판별할때도 사용이 가능하기 때문에
print(b1 and b2)

print('-' * 40)
print(1 or 2)
print(2 and 3)

# cate1의 카테고리가 0일 경우 출력하지 말고 그 외의 숫자일 경우
# 리스트를 출력
# cate1의 값에따라 비교조건을 걸어서 출력을 설정 할 수 있다.
cate1 = 0
list = ['a', 'b', 'c']
print(cate1 and list)

print('-' * 40)
# cate2와 cate3가 0이 아닌 숫자라면 list2의 내용을 출력하고
# 아닐 경우 0을 출력해주세요
cate2 = 1
cate3 = 1
list2 = ['a', 'b', 'c']
print(cate2 and cate3 and list2)
