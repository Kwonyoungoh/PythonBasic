print('Hi')
print('반가워')
print('반가워 안녕')
# 안녕 내 이름은 주석
'''
나도 주석이야.
가끔 에러나
2.xx 에서는 에러가 난다고.. 
'''


# 이게 바로 함수여
def func() -> int:
    b = 1
    c = 2
    return b + c


print(func())

# 이건 람다여
(lambda: print('this is lamda'))()
