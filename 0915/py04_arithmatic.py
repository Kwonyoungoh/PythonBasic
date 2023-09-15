a = 10
b = 3
print(a, type(a))
print(b, type(b))
print(a + b, type(a + b))
print(a - b, type(a - b))
print(a * b, type(a * b))
print(a / b, type(a / b))
print(a // b, type(a // b))

# 소수점 4자리 까지는 나오게 수식을 구성
# 그렇다면 아래와 같이
sol1 = (a * 10000) // b
print(sol1 / 10000)

# 나머지 연산
print(a % b)
print(a ** b)
