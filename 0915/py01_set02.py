s1 = {1, 2, 3, 4, 5, 6}
s2 = {4, 5, 6, 7, 8, 9}

l1 = list(s1) + list(s2)

print(set(l1))

# set의 연산
# 교집합
print(s1 & s2)
# 함수버전
print(s1.intersection(s2))
# 합집합
print(s1 | s2)
# 함수버전
print(s1.union(s2))
# 차집합
print(s1 - s2)
# 함수버전
print(s1.difference(s2))