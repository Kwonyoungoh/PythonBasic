from random import *

# 인자 a, b 사이의 난수를 생성함
i: int  = randint(1,100)
print(i)

# 인자 없을시에는 0과 1사이의 임의의 실수 생성
i2 = random()
print(i2)

# 일정 범위 내의 실수
i3 = uniform(1.0, 36.5)
print(i3)

# 1부터 100사이의 임의의 짝수
i4= randrange(0,100,2)
# step 파라미터의 배수 로 나온다
print(i4)

j: int = None
print(type(j))
j = False
print(type(j))
j = int(True)
print(j)