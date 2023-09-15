# 정수형 형변환 해주면 정수로 입력받기 가능
# 실수형 형변환은 float
# 둘중 아무거나 쓰겠다는 eval
num1: int = int(input('Decimal : '))
num2: str = input('string : ')

print(num1 * num1, type(num1))
# 아래와 같은 경우 타입 에러남
# print(num2+1, type(num2))
