a1 =True
# a == True ? 'a' : 'b'
# 파이썬의 삼항 연산자
print('a' if a1==True else 'b')

b1 = 2
# b1이 1일 경우 'a', 2일 경우 b, 아니면 c를 출력하세요
# 이런 식으로 이중으로 쓰는 경우도 있는데 가독성이 떨어짐
b2 = 'a' if  b1==1 else (b1 if b1==2 else 'c')
print(b2)